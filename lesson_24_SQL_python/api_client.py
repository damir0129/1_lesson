import requests

from credentials import BASE_URL
from lesson_19_0.conftest import fake


def auth_headers(token) -> dict:
    return {'Authorization': f"Bearer {token}"}

def login(username: str, password: str, business_role: str) -> str:
    response = requests.post(
        f"{BASE_URL}/auth/login",
        json={
            "username": username,
            "password": password,
            "business_role": business_role
        }
    )
    response.raise_for_status(200)
    return response.json()["access_token"]

def create_employee(
        student_token: str,
        email: str,
        password: str,
) -> dict:
    response = requests.post(
        f"{BASE_URL}/students/employees",
        headers=auth_headers(student_token),
        json={
            "email": email,
            "full_name": fake.full_name(),
            "password": password
        }
    )

def create_client(employee_token: str, client_data: dict) -> dict:
    response = requests.post(
        f"{BASE_URL}/employees/clients",
        headers=auth_headers(employee_token),
        json=client_data
    )

def delete_client(student_token: str, client_id: str) -> None:
    response = requests.delete(
        f"{BASE_URL}/employees/clients/{client_id}",
        headers=auth_headers(student_token)
    )
    response.raise_for_status()