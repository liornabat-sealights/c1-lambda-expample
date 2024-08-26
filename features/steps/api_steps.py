import requests
import json
from behave import given, when, then

@given('valid AWS connection')
def step_impl(context):
    # This step is a placeholder. In a real scenario, you might set up AWS credentials here.
    pass

@when('API call (No Data): \'{endpoint}\'')
def step_impl(context, endpoint):
    context.response = requests.get(f"{context.API_BASE_URL}{endpoint}")

@when('API call (Data): \'{endpoint}\'')
def step_impl(context, endpoint):
    data = json.loads(context.text)
    context.response = requests.post(f"{context.API_BASE_URL}{endpoint}", json=data)

@then('expect status: \'{status_code}\'')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code)

@then('raise: \'{exception_type}\'')
def step_impl(context, exception_type):
    response_json = context.response.json()
    assert 'errorType' in response_json
    assert response_json['errorType'] == exception_type