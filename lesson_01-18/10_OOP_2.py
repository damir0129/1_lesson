# class User:
#     def __init__(self, email, age, token):
#         self.email = email
#         self._age = age
#         self.__token = token
#
#
# user = User('test@vk.ru', 23, 'jrghbequiwbheu3141nhf13')
# print(user.email)
# print(user._age) # защищенный
# print(user._User__token) # приватный
#
# class ApiClient:
#     def __init__(self, token):
#         self.__token = token
#
#     def get_headers(self):
#         return {'Authorization': f'Bearer {self.__token}'}
#
# client = ApiClient('fqiwgjwioq')
# print(client.get_headers())

# class User:
#     def __init__(self, age):
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value < 0:
#             raise ValueError('Age cannot be negative')
#         self._age = value
#
#
# user = User(25)
# print(user.age)
# user.age = 30
# print(user.age)
#
# class ResponseWrapper:
#     def __init__(self, status_code):
#         self._status_code = status_code
#
#     @property
#     def status_code(self):
#         return self._status_code
#
#     @property
#     def is_success(self):
#         return 200 <= self._status_code < 300
#
#
# response = ResponseWrapper(201)
# print(response.status_code)
# print(response.is_success)

#
# class UserApi:
#     def get_users(self):
#         print("Real users")
#
# class MockUserApi:
#     def get_users(self):
#         print("Mock users")
#
# def run_test(api):
#     api.get_users()
#
# run_test(UserApi())
# run_test(MockUserApi())

# class AuthService:
#     def get_token(self):
#         return "token"
#
# class ApiClient:
#     BASE_URL = "https://www.googleapis.com/oauth2/v3/token"
#
#     def __init__(self):
#         self.auth_service = AuthService()
#
#     @staticmethod
#     def check_token(token):
#         if token != 0:
#             return token
#         else:
#             raise ValueError("token is invalid")
#
#     @classmethod
#     def get_url(cls):
#         return cls.BASE_URL
#
#
#     @property
#     def token(self):
#         token = self.check_token(self.auth_service.get_token())
#         return self.auth_service.get_token()
#
#     def get_headers(self):
#         return {"Authorization": f"Bearer: {self.token}"}
#
# client = ApiClient()
# print(client.get_headers())
#
# print(client.__dict__)
# print(ApiClient.__dict__)

# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return f"User(name={self.name})"
#
#     def __repr__(self):
#         return f"User('{self.name}')"
#
# user = User("Damir")
# print(user)
# print([user])

from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, login):
        self.login = login

    @abstractmethod
    def get_name(self):
        return self.login

class Admin(Person):
    def __init__(self, login):
        super().__init__(login)

    def get_name(self):
        return self.login

class User(Person):
    def __init__(self, login):
        super().__init__(login)

    def get_name(self):
        return self.login

admin = Admin('Damir')