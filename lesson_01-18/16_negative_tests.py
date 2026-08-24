from pprint import pprint

import requests
from faker import Faker
fake = Faker()

BASE_URL = "https://api.bank.easyitlab.tech"


token_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={
        "email": "damir0129@gmail.com",
        "password": "as2dwWRdBcLK"
    },
    headers={
        "Content-Type": "application/json"
    }
)

assert token_response.status_code == 200, "Failed to authenticate"
token_response_json = token_response.json()
assert isinstance(token_response_json, dict), "Response is not a dict"
assert 'access_token' in token_response_json
#
# print(token_response.json())
# print(token_response.status_code)

token = token_response_json['access_token']
assert token, "Token not found"

HEADERS = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def create_employee():
    # print("1. Creating employee")
    body = {
        'email': fake.email(),
        'full_name': fake.name(),
    }

    created_employee = requests.post(
        f'{BASE_URL}/students/employees',
        json=body,
        headers=HEADERS
    )

    pprint(created_employee.status_code)
    pprint(created_employee.json)
    pprint(dict(created_employee.headers))
    # assert created_employee.status_code == 200, (
    #     f"status code: {created_employee.status_code}",
    #     f"body: {created_employee.text}",
    # )
    created_employee_json = created_employee.json()
    pprint(created_employee_json)
    employee_id = created_employee_json.get('id')
    return employee_id
employee_id = create_employee()

created_employee = requests.get(
    f'{BASE_URL}/students/employees/{employee_id}',
    headers=HEADERS
)
get_created_employee_not_found = requests.get(
    f'{BASE_URL}/students/employees/1000000',
    headers=HEADERS
)
pprint(get_created_employee_not_found.status_code)