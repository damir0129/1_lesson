# def say_hello():
#     print("Hello World")
# say_hello()
#
# def create_user():
#     print("create user")
#     print("send request")
#     print("check status")
#
# create_user()
# create_user()

# def create_user(name, email):
#     print(f"Create user: {name}, {email}")
#
# # create_user("Damir", "admin@vk.ru")
#
# name_user = "Damir"
# email_user = "admin@vk.ru"
# create_user(name_user, email_user)

# users = {
#     "users": [
#         {
#             "name": "admin",
#             "id": 1,
#         },
#         {
#             "name": "Damir",
#             "id": 2,
#         },
#     ],
# }
#
# def get_id_user(name):
#     users_list = users["users"]
#     for user in users_list:
#         if user["name"] == name:
#             return user["id"]
#     return "Name not found"
#
# id_user = get_id_user("Damir")
# print(id_user)


# users = {
#     "users": [
#         {
#             "name": "admin",
#             "age": 14,
#             "id": 1
#         },
#         {
#             "name": "Damir",
#             "age": 22,
#             "id": 2
#         },
#         {
#             "name": "Ivan",
#             "age": 18,
#             "id": 3
#         },
#     ],
# }
#
# def has_adult(age):
#     users_list = users["users"]
#     ids_adult = []
#     for user in users_list:
#         if user["age"] >= 18:
#             ids_adult.append(user["id"])
#     return ids_adult
#
# ids_list = has_adult(18)
# print(ids_list)

# def retry_request(count):
#     attempts = count
#     while attempts > 0:
#         print("Send request")
#         attempts -= 1
#
# retry_request(3)

# def create_user():
#     user_id = 100
#     return user_id
#
# user_id = create_user()
# print(user_id)

def retry_request(count=5):
    attempts = count
    while attempts > 0:
        print("Send request")
        attempts -= 1

retry_request()