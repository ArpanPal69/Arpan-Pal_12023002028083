import os
from dotenv import load_dotenv
from utils.api_client import APIClient

def before_all(context):
    load_dotenv()
    
    base_url = context.config.userdata.get("BASE_URL") or os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    
    print("Fetching dynamic auth token for current environment...")
    auth_token = os.getenv("AUTH_TOKEN")
    
    context.api = APIClient(base_url, auth_token)
    print(f"Test Suite Execution Started on URL: {base_url}")

def after_scenario(context, scenario):
    if "Create a new user" in scenario.name and hasattr(context, "response"):
        if context.response.status_code == 201:
            user_id = context.response.json().get("id")
            if user_id:
                print(f"TEARDOWN: Automatically deleting dynamically generated user with ID {user_id}")
                context.api.delete(f"/users/{user_id}")
