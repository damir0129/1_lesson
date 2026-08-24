# class User:
#     pass
#
# user1 = User()

#
# class User:
#     def __init__(self, email, password):
#         print("self: ", id(self))
#         self.email = email
#         self.password = password
#
#     def login(self):
#         print("login with ", self.email)
#
#
# user = User("test@vk.ru", "pass")
# # print("user: ", user.email)
# #
# # print(type(user))
# user.login()
#
# lst = [1, 2, 3]
# lst.append(4)
#
# class ApiClass:
#     base_url = "http://127.0.0.1:8000"
#
# client = ApiClass()
#
# print(client.base_url)

# class User:
#     role = "user"
#
# u1 = User()
# u2 = User()
#
# print(id(u1.role))
# print(id(u2.role))
#
# u1.role = "admin"
#
# print(id(u1.role))
# print(id(u2.role))
#

# class A:
#     x = 10
#
# a = A()
# b = A()
#
# a.x = 20
#
# print(a.x, b.x)
#
# class User:
#     def __init__(self, email):
#         self.email = email
#
# user = User("test@vk.ru")
# print(id(user))
#
# user.email = "admin@vk.ru"
# print(id(user))
#
# class User:
#     pass
#
# user = User()
# print(user.__dict__)
#
# user.email = "admin@vk.ru"
#
# print(user.__dict__)

# class Cart:
#     def __init__(self):
#         self.items = []
#
#
# cart1 = Cart()
# cart2 = Cart()
#
# cart1.items.append("laptop")
#
# print(cart1.items)
# print(cart2.items)

# class API:
#     def request(self, method, url):
#         print("BaseAPI:", method, url)
#
# class BaseAPI(API):
#     def request(self, method, url):
#         print("Change method:", method, url)
#
#
# class UserAPI(BaseAPI, API):
#     def get_users(self):
#         self.request("GET", "/users")
#
# api = UserAPI()
# api.get_users()
#
# print(UserAPI.__mro__)


class BaseAPI:
    def request(self):
        print("BaseAPI")

class UserAPI(BaseAPI):
    def request(self):
        super().request()
        print("UserAPI")

api = UserAPI()

api.request()


class User:
    def __init__(self):
        pass

user = User()