import requests

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

