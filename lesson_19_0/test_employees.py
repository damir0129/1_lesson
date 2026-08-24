import requests
from faker import Faker
fake = Faker()

def test_get_employee_success(base_url, auth_headers):
    employees = requests.get(
        f"{base_url}/students/employees",
        headers=auth_headers,
    )

    assert employees.status_code == 200, (
        f'Expected: 200\n'
        f"Actual: {employees.status_code}"
    )

    employees_json = employees.json()
    assert isinstance(employees_json, list)

def test_created_employee(base_url, auth_headers):
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

def test_get_employee(auth_headers, base_url, created_employee):
    id_employee, email, full_name = created_employee

    employee = requests.get(
        f"{base_url}/students/employees/{id_employee}",
        headers=auth_headers,
    )

    assert employee.status_code == 200, ()

    employee_json = employee.json()

    assert employee_json['email'] == email
    assert employee_json['full_name'] == full_name