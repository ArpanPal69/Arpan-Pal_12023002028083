from behave import given, when, then
from utils.payloads import create_user_payload
from jsonschema import validate
from utils.schemas import user_schema

@given('the user endpoint "{endpoint}" is available')
def step_impl(context, endpoint):
    context.endpoint = endpoint

@when('I send a GET request to fetch the user')
def step_impl(context):
    context.response = context.api.get(context.endpoint)

@when('I send a POST request with name "{name}", username "{username}", and email "{email}"')
def step_impl(context, name, username, email):
    payload = create_user_payload(name, username, email)
    
    # Save the dynamically generated name for the assertion later (in case it was 'random')
    context.expected_name = payload["name"] 
    context.response = context.api.post(context.endpoint, payload)

@then('the response status code should be {status_code:d}')
def step_impl(context, status_code):
    actual_code = context.response.status_code
    assert actual_code == status_code, f"Expected {status_code}, but got {actual_code}"

@then('the response should contain the user name "{expected_name}"')
def step_impl(context, expected_name):
    json_data = context.response.json()
    
    # 1. API Contract Testing (JSON Schema Validation)
    validate(instance=json_data, schema=user_schema)
    
    # 2. Dynamic Value Validation (checking if we used Faker)
    name_to_check = context.expected_name if expected_name == "random" else expected_name
    
    actual_name = json_data.get('name')
    assert actual_name == name_to_check, f"Expected {name_to_check}, got {actual_name}"
