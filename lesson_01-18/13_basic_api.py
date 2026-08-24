"""

mobile app > backend service > backend processing > mobile app
browser > backend service > backend processing > browser app

"""

import requests

BASE_URL = "https://api.bank.easyitlab.tech"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMmY1MTRkYy1iZjVjLTQ4MDMtOTE4MC0zZTQ1NDlkMGI4MWQiLCJ1c2VyX2lkIjoiMTJmNTE0ZGMtYmY1Yy00ODAzLTkxODAtM2U0NTQ5ZDBiODFkIiwic3lzdGVtX3JvbGUiOiJTVFVERU5UIiwiYnVzaW5lc3Nfcm9sZSI6IkNMSUVOVCIsInBlcm1pc3Npb25zIjpbImNsaWVudDphY2NvdW50czpyZWFkIiwiY2xpZW50OnRyYW5zZmVyczpjcmVhdGUiLCJjbGllbnQ6dGlja2V0czpjcmVhdGUiXSwic2Vzc2lvbl9pZCI6IjhkN2MxYTVkMzc2MTQ4YjI5MjM5YzFjZTJhMTNkY2JkIiwiaWF0IjoxNzgzMjQ1MDE5LCJleHAiOjE3ODMyNDU5MTksInR5cGUiOiJhY2Nlc3MifQ.QkVeCbm6NTX1ClX83e27gEJcy5R66erDoJCWKNXyDXU"

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

created_employee = requests.post(
    url=f"{BASE_URL}/students/employees",
    headers=headers,
    json=body
)
created_employee_json = created_employee.json()

print(created_employee.status_code)
print(type(created_employee_json))
print(created_employee_json)

assert created_employee.status_code == 200, "Не успешно"
assert isinstance(created_employee_json, dict)
assert created_employee_json.get("id") is not None