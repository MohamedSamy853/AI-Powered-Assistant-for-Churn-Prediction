# AI-Powered Assistant for Churn Prediction

## Overview

This project is focused on building a Proof of Concept (PoC) to demonstrate how AI, specifically a Large Language Model (LLM), can be utilized to analyze customer stories and extract relevant information that can be passed to a classification model for predicting customer churn. The goal is to create an intuitive interface that allows clients, particularly those in non-technical roles, to interact with the AI in a natural way, by explaining their situation as a story, and receive predictions on whether a customer will churn or not.

## Business Value

The business value of this solution lies in its ability to make AI more accessible and user-friendly for clients. By allowing the AI to understand and process natural language input, the model can extract key information from a client's story and pass it to a churn prediction model. This approach simplifies the interaction with AI, making it easier for clients to get actionable insights without needing to understand the technical complexities behind the model.

## Objectives

- **Churn Classification Model**: Demonstrate expertise in constructing a classical machine learning model for predicting customer churn.
- **LLM Integration**: Utilize an LLM to interact with the classification model, enabling natural language queries and responses.
- **API and Chatbot Pipeline**: Develop a pipeline to handle chat interactions with the classification model, making it easy for the marketing team to input queries and receive understandable results.

## Use Cases

- **Client Interaction**: Clients can describe their situation or customer profile in a narrative format. The AI will process this input, extract relevant data, and predict whether the customer is likely to churn.
- **Predictive Analysis**: The AI system predicts customer behavior based on the extracted information, providing valuable insights into potential churn.
- **Ease of Use**: The solution is designed to make it easy for non-technical users to interact with the AI, helping them understand and utilize predictive analytics effectively.

## How the Solution Meets the Client's Requirements

- **Natural Language Processing**: The solution leverages LLMs to translate marketing questions and customer stories into structured data that the classification model can use.
- **User-Friendly Interface**: The AI presents results in a clear and understandable format, making it accessible to the marketing team without requiring deep technical knowledge.
- **Predictive Accuracy**: By using a classical machine learning model, the solution provides reliable churn predictions based on the input data.

## Tools and Libraries

- **LangChain**: To enable interaction with the LLM and manage the conversation flow.
- **HuggingFace Hub**: To access open-source LLMs such as LLaMA 3:8B for text processing and data extraction.
- **scikit-learn**: To build the churn classification model.
- **FastAPI**: To create the API that will handle client requests and interact with the LLM and classification model.
- **Uvicorn**: To run the FastAPI application server.

## Diagram

The diagram illustrates the components and flow of data in the solution:

1. **Client Interaction**: The client provides a story in natural language.
2. **LLM Processing**: The LLM processes the story, extracting relevant features.
3. **Data Mapping**: The extracted features are mapped to numerical values (e.g., categorical features are encoded).
4. **Churn Prediction Model**: The processed data is fed into the churn prediction model.
5. **API**: The API handles the communication between the client, LLM, and churn model.
6. **Response**: The model's prediction is sent back to the client in a clear, understandable format.

## Dataset Overview

- **Mapping Categorical Features**: Categorical features are mapped to numerical values for the model.
- **Data Type Casting**: Data types are cast appropriately, ensuring compatibility with the model.
- **Handling Errors in `Total_Charges`**: The `Total_Charges` feature contained errors (empty strings), which were treated as null values and dropped from the dataset since the number of affected rows was minimal and did not significantly impact the dataset's size.

## How to Use
   ```bash
   git clone https://github.com/MohamedSamy853/AI-Powered-Assistant-for-Churn-Prediction
   cd AI-Powered-Assistant-for-Churn-Prediction
   pip install -r requirements.txt
   uvicorn main:app
```
## Example 
```python
import pytest
import requests

payload = {
    'text': 'Jane Smith is a Female customer who is 70 years old and is a senior citizen. She has been with the company for 12 months. Jane is married and has two children. She does not have a phone service but has a dual-line connection. Her internet service provider is DSL. She has online security enabled but does not have online backup or device protection. She does receive technical support and subscribes to streaming TV but not to streaming movies. Jane has a two-year contract and prefers receiving paper bills. She pays through a mailed check, with monthly charges of 60.2, and her total charges so far are 722.4.'
}

expected_output = 'No'

url = 'http://127.0.0.1:8000/predict'

output = requests.get(url=url, params=payload)

def test_sample():
    assert output.json()['churn'] == expected_output, 'There is an error'
```


