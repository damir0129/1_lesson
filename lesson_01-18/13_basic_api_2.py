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
    print("1. Creating employee")
    body = {
        'email': fake.email(),
        'full_name': fake.name(),
    }

    created_employee = requests.post(
        f'{BASE_URL}/students/employees',
        json=body,
        headers=HEADERS
    )
    assert created_employee.status_code == 200, "Failed to create employee"
    created_employee_json = created_employee.json()
    employee_id = created_employee_json.get('id')
    return employee_id

def delete_employee(employee_id):
    print("2. Deleting employee")
    deleted_employee = requests.delete(
        f'{BASE_URL}/students/employees/{employee_id}',
        headers=HEADERS
    )
    assert deleted_employee.status_code == 200, "Failed to delete employee"

def test_employee_lifecycle():
    print("3. Start Test")
    employee_id = create_employee()
    delete_employee(employee_id)
    print("4. End Test")

test_employee_lifecycle()