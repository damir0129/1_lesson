"Task 1"
from unittest import TestResult


class TestRunStats:
    def __init__(self, failed_tests=None):
        if failed_tests is None:
            self._failed_tests = []
        else:
            self._failed_tests = failed_tests


    def add_failed_test(self, test_name: str):
        self._failed_tests.append(test_name)

    def add_failed_tests(self, test_names: list):
        self._failed_tests.extend(test_names)

    def get_failed_tests(self) -> list:
        return self._failed_tests

    def get_failed_count(self) -> int:
        return len(self._failed_tests)

run1 = TestRunStats()
run2 = TestRunStats()
run1.add_failed_test("test_create_user")
run1.add_failed_tests(["test_delete_user", "test_update_user"])
print(run1.get_failed_tests())
print(run1.get_failed_count())
print(run2.get_failed_tests())

"Task 2"
class EnvironmentConfig:
    DEFAULT_TIMEOUT = 30
    def __init__(self, env_name, base_url, api_key):
        self.env_name = env_name
        self.base_url = base_url
        self.__api_key = api_key

    @property
    def api_key_masked(self):
        return self.__api_key[:3] + "***"

    @property
    def base_api_url(self):
        return self.base_url

    @staticmethod
    def is_valid_url(url: str):
        return bool(url) and url.startswith("http")

    @classmethod
    def get_default_timeout(cls):
        return cls.DEFAULT_TIMEOUT

config = EnvironmentConfig("stage", "https://stage.api.test.com", "abcdef123456")
print(config.base_api_url)
print(config.api_key_masked)
print(EnvironmentConfig.is_valid_url("https://test.com"))
print(EnvironmentConfig.get_default_timeout())

"Task 3"
class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class TestReporter():
    def __init__(self):
        self.logger = Logger()
        self.results = []

    def add_result(self, test_name: str, status: str) -> None:
        message = f"Test: {test_name}, Status: {status}"
        self.logger.log(message)
        self.results.append(message)

    def show_results(self):
        print("\n--- Final Results ---")
        for result in self.results:
            print(result)

reporter = TestReporter()
reporter.add_result("test_login", "passed")
reporter.add_result("test_delete_user", "failed")
reporter.show_results()

"Task 4"
class DictDataSource:
    def __init__(self, test_data: dict):
        self.test_data = test_data

    def get_data(self):
        return self.test_data

class MockDataSource:
    def get_data(self):
        return {"email": "mock@test.com", "password": "123456"}

def prepare_login_data(data_source):
    data_dict = data_source.get_data()
    print(f"Keys: {list(data_dict.keys())}")
    return data_dict

def transform_data(func) -> dict:
    raw_dict = func()
    upper_dict = {}
    for key, value in raw_dict.items():
        if isinstance(value, str):
            upper_dict[key] = value.upper()
        else:
            upper_dict[key] = value
    return upper_dict

real_source = DictDataSource({"email": "user@test.com", "password": "qwerty"})
mock_source = MockDataSource()
print(prepare_login_data(real_source))
# Keys: ['email', 'password'] - это печатается из prepare_login_data
# {'email': 'user@test.com', 'password': 'qwerty'} - это возвращается
print(prepare_login_data(mock_source))
# Keys: ['email', 'password'] - это печатается из prepare_login_data
# {'email': 'mock@test.com', 'password': '123456'} - это возвращается
print(real_source.get_data())
# {'email': 'user@test.com', 'password': 'qwerty'}
print(mock_source.get_data())
# {'email': 'mock@test.com', 'password': '123456'}
upper_data = transform_data(mock_source.get_data)
print(upper_data)
# {'email': 'MOCK@TEST.COM', 'password': '123456'}


"Task 5"

from abc import ABC, abstractmethod

class BaseCheck(ABC):
    @abstractmethod
    def check(self, response: dict) -> bool:
        pass

class StatusCodeCheck(BaseCheck):
    def __init__(self, expected_status_code: int):
        self.expected_status_code = expected_status_code

    def check(self, response: dict) -> bool:
        return response["status_code"] == self.expected_status_code

class RequiredFieldCheck(BaseCheck):
    def __init__(self, field_name: str):
        self.field_name = field_name
    def check(self, response: dict) -> bool:
        return self.field_name in response["body"]

def run_checks(checks: list, response: dict) -> list[bool]:
    results_list = []
    for check in checks:
        result = check.check(response)
        results_list.append(result)
    return results_list

response = {
    "status_code": 200,
    "body": {
        "id": 1,
        "name": "Daniil"
    }
}
status_check = StatusCodeCheck(200)
field_check_id = RequiredFieldCheck("id")
field_check_email = RequiredFieldCheck("email")
print(status_check.check(response)) # True
print(field_check_id.check(response)) # True
print(field_check_email.check(response)) # False
checks = [
StatusCodeCheck(200),
RequiredFieldCheck("id"),
RequiredFieldCheck("email")
]
results = run_checks(checks, response)
print(results)
# [False, True, True