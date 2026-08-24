import requests
import pytest

from faker import Faker
fake = Faker()

@pytest.fixture(scope='session')
def base_url():
    base_url = "https://api.bank.easyitlab.tech"
    return base_url

@pytest.fixture(scope='session')
def access_token(base_url):
    access_token_response = requests.post(
        f"{base_url}/auth/login",
        json={
            "email": "damir0129@gmail.com",
            "password": "as2dwWRdBcLK"
        },
        headers={
            "Content-Type": "application/json"
        }
    )

    assert access_token_response.status_code == 200, "Failed to authenticate"
    access_token_response_json = access_token_response.json()

    assert isinstance(access_token_response_json, dict), "Response is not a dict"

    access_token = access_token_response_json['access_token']
    assert access_token, "access_token not found"
    return access_token

@pytest.fixture
def auth_headers(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return headers

@pytest.fixture
def created_employee(auth_headers, base_url):
    email = fake.email()
    full_name = fake.name()

    payload = {
        "email": email,
        "full_name": full_name,
    }

    created_employee = requests.post(
        f"{base_url}/students/employees",
        json=payload,
        headers=auth_headers,
    )

    assert created_employee.status_code == 200

    created_employee_json = created_employee.json()

    assert created_employee_json['email'] == email
    assert created_employee_json['full_name'] == full_name

    yield (
        created_employee_json['id'],
        created_employee_json['email'],
        created_employee_json['full_name']
    )

    deleted_employee = requests.delete(
        f"{base_url}/students/employees/{created_employee_json['id']}",
        headers=auth_headers,
    )