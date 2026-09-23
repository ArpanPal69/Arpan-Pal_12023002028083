import requests
import allure
import json

class APIClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        # INNOVATION 1: Connection Pooling for faster execution
        self.session = requests.Session()
        self.session.headers.update({'Content-type': 'application/json; charset=UTF-8'})
        
        if token:
             self.session.headers.update({'Authorization': token})

    # INNOVATION 2: Auto-attaching logs to Allure
    def _log_to_allure(self, method, endpoint, response, payload=None):
        allure.attach(
            body=f"URL: {self.base_url}{endpoint}\nPayload: {json.dumps(payload, indent=2)}\n\nResponse Code: {response.status_code}\nResponse Body: {response.text}",
            name=f"{method} Request to {endpoint}",
            attachment_type=allure.attachment_type.TEXT
        )

    def get(self, endpoint):
        response = self.session.get(f"{self.base_url}{endpoint}")
        self._log_to_allure("GET", endpoint, response)
        return response

    def post(self, endpoint, payload):
        response = self.session.post(f"{self.base_url}{endpoint}", json=payload)
        self._log_to_allure("POST", endpoint, response, payload)
        return response
        
    def delete(self, endpoint):
        response = self.session.delete(f"{self.base_url}{endpoint}")
        self._log_to_allure("DELETE", endpoint, response)
        return response
