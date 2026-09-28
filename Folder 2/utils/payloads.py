from faker import Faker

fake = Faker()

def create_user_payload(name, username, email):
    return {
        "name": fake.name() if name == "random" else name,
        "username": fake.user_name() if username == "random" else username,
        "email": fake.email() if email == "random" else email
    }
