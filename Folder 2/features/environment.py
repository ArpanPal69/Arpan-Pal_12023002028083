import os
from dotenv import load_dotenv
from utils.api_client import APIClient

def before_all(context):
    load_dotenv()
    
    # UPDATE 1: Cross-Environment Execution (reads from terminal '-D BASE_URL', falls back to .env)
    base_url = context.config.userdata.get("BASE_URL") or os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
    
    # UPDATE 2: Simulated Dynamic Auth
    # In a real company, we would do: response = requests.post(f"{base_url}/login")
    # For this public API, we safely simulate it by grabbing from env to avoid breaking the test
    print("Fetching dynamic auth token for current environment...")
    auth_token = os.getenv("AUTH_TOKEN")
    
    # Initialize the reusable API client
    context.api = APIClient(base_url, auth_token)
    print(f"Test Suite Execution Started on URL: {base_url}")

def after_scenario(context, scenario):
    # UPDATE 3: Automated Database Cleanup (Teardown State)
    # If a POST test generated a new user, delete them to prevent database pollution
    if "Create a new user" in scenario.name and hasattr(context, "response"):
        if context.response.status_code == 201:
            user_id = context.response.json().get("id")
            if user_id:
                print(f"TEARDOWN: Automatically deleting dynamically generated user with ID {user_id}")
                context.api.delete(f"/users/{user_id}")
