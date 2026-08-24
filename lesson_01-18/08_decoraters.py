users = {
    "users": [
        {
            "name": "admin",
            "age": 14,
            "id": 1
        },
        {
            "name": "Damir",
            "age": 22,
            "id": 2
        },
        {
            "name": "Ivan",
            "age": 18,
            "id": 3
        },
    ],
}
#
# names = []
# for user in users["users"]:
#     names.append(user["name"])

# names = [user["name"] for user in users["users"]]
#
# names = [user["name"] for user in users["users"] if user["age"] > 18]
#
# print(names)

# orders = {
#     "orders": [
#         {
#             "id": 1,
#             "status": "paid",
#         },
#         {
#             "id": 2,
#             "status": "paid",
#         },
#         {
#             "id": 3,
#             "status": "cancelled",
#         },
#     ]
# }
#
# paid_orders = [order["id"] for order in orders["orders"] if order["status"] == "paid"]
#
# print(paid_orders)
#
# cancelled_orders = [order["id"] for order in orders["orders"] if order["status"] == "cancelled"]
#
# print(cancelled_orders)


# def decorator(func):
#     def wrapper():
#         print("Start function")
#         func()
#         print("End function")
#     return wrapper
#
#
# @decorator
# def get_id_users():
#     print(123)
#
# get_id_users()

# print(get_id_users())


# def logger(func):
#     def wrapper(*args, **kwargs):
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("func:", func)
#         print("Start function")
#         result = func(*args, **kwargs)
#         print("End function")
#         return result
#     return wrapper
#
# @logger
# def get_id_users(name, email):
#     for user in users["users"]:
#         if user["name"] == name:
#             return user["id"]
#
# name = "Damir"
# email_user = "admin@vk.ru"
#
# print(get_id_users(name, email=email_user))

def id_name(*args, **kwargs):
    print("args:", args)
    print("kargs:", kwargs)

id_name(123, ("asd", True), name="Damir", age=22)