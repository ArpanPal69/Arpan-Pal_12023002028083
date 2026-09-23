# JSON Schema for strict API contract testing
user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["id", "name", "username", "email"]
}
