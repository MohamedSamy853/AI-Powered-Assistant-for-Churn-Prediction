import pytest

import requests

payload = {'text':'Jane Smith is a Female customer who is 70 years old and is a senior citizen. She has been with the company for 12 months. Jane is married and has two children. She does not have a phone service but has a dual-line connection. Her internet service provider is DSL.  She has online security enabled but does not have online backup or device protection. She does receive technical support and subscribes to streaming TV but not to streaming movies. Jane has a two-year contract and prefers receiving paper bills. She pays through a mailed check, with monthly charges of 60.2, and her total charges so far are 722.4.'}

expected_output = 'No'

url = 'http://127.0.0.1:8000/predict'



output = requests.get(url=url, params=payload)

def test_sample():
    assert output.json()['churn'] == expected_output , 'There are an error'
