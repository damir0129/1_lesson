"""

mobile app > backend service > backend processing > mobile app
browser > backend service > backend processing > browser app

"""

from faker import Faker
fake = Faker()
import requests

BASE_URL = "https://api.bank.easyitlab.tech"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMmY1MTRkYy1iZjVjLTQ4MDMtOTE4MC0zZTQ1NDlkMGI4MWQiLCJ1c2VyX2lkIjoiMTJmNTE0ZGMtYmY1Yy00ODAzLTkxODAtM2U0NTQ5ZDBiODFkIiwic3lzdGVtX3JvbGUiOiJTVFVERU5UIiwiYnVzaW5lc3Nfcm9sZSI6IkNMSUVOVCIsInBlcm1pc3Npb25zIjpbImNsaWVudDphY2NvdW50czpyZWFkIiwiY2xpZW50OnRyYW5zZmVyczpjcmVhdGUiLCJjbGllbnQ6dGlja2V0czpjcmVhdGUiXSwic2Vzc2lvbl9pZCI6IjUzNDBkYWZhNmFhMzQzNTg5ZDBhNDNjY2I1OTgyNDgyIiwiaWF0IjoxNzgzNDAzMTQ0LCJleHAiOjE3ODM0MDQwNDQsInR5cGUiOiJhY2Nlc3MifQ.hwKas2LYkd_fdi5fmt757O98taM72GqDPVy38Vunxw4"

# headers = {
#     'Authorization': f'Bearer {TOKEN}',
#     'Content-Type': 'application/json'
# }
#
# response = requests.get(
#     url=f"{BASE_URL}/students/employees",
#     headers=headers
# )
#
# print(response.status_code)
# print(type(response.json()))
# print(response.json())

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

body = {
    "email": "py3@localhost",
    "full_name": "Damir Ignatev"
}

# created_employee = requests.post(
#     url=f"{BASE_URL}/students/employees",
#     headers=headers,
#     json=body
# )
# created_employee_json = created_employee.json()
#
# print(created_employee.status_code)
# print(type(created_employee_json))
# print(created_employee_json)


# assert isinstance(created_employee_json, dict)

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Content-Type': 'application/json'
}

def test_api_users_https():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS,
    )

    assert response.url.startswith("https://")

def get_dashboard():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS,
    )

    assert response.url.startswith("https://")
    return response.json()


test_api_users_https()

def test_dashboard_employee_create():
    before = get_dashboard()

    payload = {
        'email': fake.email(),
        'full_name': fake.name(),
    }

    requests.post(
        f"{BASE_URL}/students/employees",
        headers=HEADERS,
        json=payload,
    )

    after = get_dashboard()

    # Отладка: смотрим, что реально вернул сервер
    print("Структура ответа after:", after)

    # Безопасное получение значения (вернет None, если ключа нет)
    after_total = after.get('employees_total')
    before_total = before.get('employees_total')

    print(f"Before: {before_total}, After: {after_total}")

    assert after_total >= before_total


# test_dashboard_employee_create()

def get_response_dashboard():
    response = requests.get(
        f"{BASE_URL}/students/dashboard",
        headers=HEADERS,
    )

    assert response.url.startswith("https://")
    return response

def test_rate_limiting():
    status = 200
    counter = 0
    while status != 429:
        status = get_response_dashboard().status_code
        counter += 1

    return counter

counter = test_rate_limiting()

print(counter)