import unittest
from wsgiref import headers

import requests


BASE_URL = "https://api.bank.easyitlab.tech"

def get_token():
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
    return token

def get_auth_headers():
    headers = {
        "Authorization": f"Bearer {get_token()}",
        "Content-Type": "application/json"
    }
    return headers


class TestStudentDashboard(unittest.TestCase):

    def ttest_get_dashboard_success(self):
        headers = get_auth_headers()

        students_dashboard = requests.get(
            f"{BASE_URL}/students/dashboard",
            headers=headers,
        )

        self.assertEqual(students_dashboard.status_code, 200, "Failed to get dashboard")

        students_dashboard_json = students_dashboard.json()

        self.assertIn('employees_total', students_dashboard_json)
        self.assertIn('clients_total', students_dashboard_json)
        self.assertIn('accounts_total', students_dashboard_json)
        self.assertIn('tickets_total', students_dashboard_json)


if __name__ == '__main__':
    unittest.main()
else:
    print("__name__",__name__)