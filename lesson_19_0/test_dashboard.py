from pprint import pprint
from unittest.mock import Mock

import pytest
import requests
import allure

@allure.feature("Dashboard")
@allure.story("Get dashboard")
@allure.title("Get dashboard")
@allure.description("Check dashboard")

def test_get_dashboard_success(auth_headers, base_url):
    students_dashboard = requests.get(
        f"{base_url}/students/dashboard",
        headers=auth_headers,
    )

    assert students_dashboard.status_code == 200

    students_dashboard_json = students_dashboard.json()

    assert 'employees_total' in students_dashboard_json
    assert 'clients_total' in students_dashboard_json
    assert 'accounts_total' in students_dashboard_json
    assert 'tickets_total' in students_dashboard_json

class FakeDashboardResponse:
    status_code = 200

    def json(self):
        return {'accounts_total': 15,
         'clients_total': 5,
         'employees_active': 16,
         'employees_blocked': 1,
         'employees_total': 18,
         'series': [{'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-20',
                     'employees': 0,
                     'tickets': 0},
                    {'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-21',
                     'employees': 0,
                     'tickets': 0},
                    {'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-22',
                     'employees': 0,
                     'tickets': 0},
                    {'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-23',
                     'employees': 0,
                     'tickets': 0},
                    {'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-24',
                     'employees': 9,
                     'tickets': 0},
                    {'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-25',
                     'employees': 2,
                     'tickets': 0},
                    {'accounts': 0,
                     'clients': 0,
                     'day': '2026-08-26',
                     'employees': 0,
                     'tickets': 0}],
         'tickets_total': 11,
         'transfers_total': 0}

@allure.feature("Dashboard")
@allure.story("Mock and monkeypatch")
@allure.title("Get dashboard with stub")
@allure.description("Check dashboard")
def test_get_dashboard_with_stub(monkeypatch, auth_headers, base_url):
    def fake_get(url, headers):
        return FakeDashboardResponse()

    monkeypatch.setattr(requests, 'get', fake_get)

    with allure.step("Send GET /students/dashboard"):
        students_dashboard = requests.get(
            f"{base_url}/students/dashboard",
            headers=auth_headers,
        )

    with allure.step(f"Check status code 200"):
        assert students_dashboard.status_code == 200

    with allure.step(f"Check response body"):
        students_dashboard_json = students_dashboard.json()

    assert "employees_total" in students_dashboard_json
    assert "clients_total" in students_dashboard_json
    assert "accounts_total" in students_dashboard_json
    assert "tickets_total" in students_dashboard_json


@allure.feature("Dashboard")
@allure.story("Mock and monkeypatch")
@allure.title("Get dashboard with Mock")
@allure.description("Check dashboard from Mock")
def test_get_dashboard_with_mock(monkeypatch, auth_headers, base_url):
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {'accounts_total': 15,
                                         'clients_total': 5,
                                         'employees_active': 16,
                                         'employees_blocked': 1,
                                         'employees_total': 18,
                                         'tickets_total': 11,
                                         'transfers_total': 0}
    requests_get_mock = Mock(return_value=fake_response)
    monkeypatch.setattr(requests, 'get', requests_get_mock)

    with allure.step("Send GET /students/dashboard"):
        students_dashboard = requests.get(
            f"{base_url}/students/dashboard",
            headers=auth_headers,
        )

    with allure.step(f"Check status code 200"):
        assert students_dashboard.status_code == 200

    with allure.step(f"Check response body"):
        students_dashboard_json = students_dashboard.json()

        assert "employees_total" in students_dashboard_json
        assert "clients_total" in students_dashboard_json
        assert "accounts_total" in students_dashboard_json
        assert "tickets_total" in students_dashboard_json

    with allure.step(
                'Check requests.get was called with correct url and headers'
    ):
        requests_get_mock.assert_called_with(
            f"{base_url}/students/dashboard",
            headers=auth_headers,
        )

    with allure.step("Check json method was called"):
        fake_response.json.assert_called_once()


@allure.feature("Dashboard")
@allure.story("Mock and monkeypatch")
@allure.title("Dashboard requests failed")
@allure.description("Check dashboard from Mock")
def test_get_dashboard_requests_failed(monkeypatch, auth_headers, base_url):
    requests_get_mock = Mock(
        side_effect=requests.ConnectionError("Service unavailable")
    )
    monkeypatch.setattr(requests, 'get', requests_get_mock)

    with pytest.raises(requests.ConnectionError):
        requests.get(f"{base_url}/students/dashboard", headers=auth_headers)

    requests_get_mock.assert_called_once_with(
        f"{base_url}/students/dashboard",
        headers=auth_headers,
    )