from src.model import get_model
from src.format_outputs import prep_item
from fastapi import FastAPI
from src.model_pipeline import get_classification_model


model = get_classification_model()

llm = get_model()

app = FastAPI()

prompt ='''
**Task:** Extract and return customer information in a specific order as a list.
only return list not add any information or notes or anything.


**Instructions:**
1. **Extract the following features from the provided query in the exact order listed below.**
2. **For each feature, select the value from the given options only.**
3. **Return the values as a Python list in the specified order. Ensure the values are case-sensitive and match exactly as described in the options.**

**Order of Features and Allowed Values:**
1. **Gender**: 0 if 'Male' or 1 if 'Female'
2. **Senior_citizen**: 1 (for Yes) or 0 (for No)
3. **Is_married**: 1 for 'Yes' or 0 for 'No'
4. **Dependents**: 1 for 'Yes' or 0 for 'No'
5. **Tenure**: A number representing the number of months
6. **Phone_service**: 1 for 'Yes' or 0 for 'No'
7. **Dual**: 1 for 'Yes' or 0 for 'No'
8. **Internet_service**: 1 for 'DSL', 2 for 'Fiber optic', or 0 for 'No'
9. **Online_security**: 1 for 'Yes', 0 for 'No', or 2 for 'No internet service'
10. **Online_backup**: 1 for 'Yes', 0 for  'No', or 2 for 'No internet service'
11. **Device_protection**: 1 for 'Yes', 0 for 'No', or 2 for 'No internet service'
12. **Tech_support**: 1 for 'Yes', 0 for 'No', or 2 for 'No internet service'
13. **Streaming_tv**: 1 for 'Yes', 0 for 'No', or 2 for 'No internet service'
14. **Streaming_movies**: 1 for 'Yes', 0 for 'No', or 2 for 'No internet service'
15. **Contract**: 0 for 'Month-to-month', 1 for 'One year', or 2 for 'Two year'
16. **Paperless_billing**: 1 for 'Yes' or 0 for 'No'
17. **Payment_method**: 0 for 'Electronic check', 1 for 'Mailed check', 2 for 'Bank transfer (automatic)', or 3 for 'Credit card (automatic)'
18. **Monthly_charges**: A number representing the monthly charges
19. **Total_charges**: A number representing the total charges

Important:

-The list must strictly follow the order mentioned.
-All categorical values must match the provided options exactly.
-Do not return any additional text or explanation, only the list.
-All values in List must be number you should map every category for matched number as mention.

customer information :

{content}

'''

@app.get("/predict")
def predict(text:str):
    
    input_prompt = prompt.format(content = text)
    
    res = llm.invoke(input_prompt)
    
    listed_res = eval(res)
    
    item = prep_item(listed_res)
    
    output = model.predict(item)
    
    print("==========")
    print(output)
    print("===========")
    
    return {"churn":'No' if output[0]==0 else 'Yes'}
    
    
    

