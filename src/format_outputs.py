import pandas as pd

column_names = ['Gender', 'Senior_citizen', 'Is_married', 'Dependents',
       'Tenure', 'Phone_service', 'Dual', 'Internet_service',
       'Online_security', 'Online_backup', 'Device_protection', 'Tech_support',
       'Streaming_tv', 'Streaming_movies', 'Contract', 'Paperless_billing',
       'Payment_method', 'Monthly_charges', 'Total_charges']

def prep_item(lis):
    sample = pd.DataFrame(data = {col:val for col , val in zip(column_names , lis)} , index=[0])
    
    return sample

