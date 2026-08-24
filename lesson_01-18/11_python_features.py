# import os
#
# import datetime
#
# print(datetime.datetime.now())
# print(datetime.timedelta(days=10, hours=10))
#
# import random
#
# from random import randint, random, randrange, choice
#
# print(randrange(0, 100))
# print(randint(0, 100))
# print(random())
# print(choice([1, 100]))
import datetime
# file = open('11_email.txt', 'r')
# emails = file.readlines()
# file.close()
# for email in emails:
#     print(email)

# with open('11_email.txt', 'r') as f:
#     emails = f.read()
#
# print(emails)

# class OpenFile:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#     def __enter__(self):
#         self.f = open(self.filename, self.mode)
#         return self.f
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.f:
#             self.f.close()
#
# with OpenFile('11_email.txt', 'a') as f:
#     f.write('\nexample@example.com')

import os

# from urllib3.contrib.emscripten import response

base_path = os.path.dirname( __file__ )
file_path = os.path.join(base_path, '11_app.log')

# with open(file_path, 'r') as f:
#     logs = f.readlines()

# print(logs)
# assert 'ERROR' not in logs, (
#     "Errors in log",
#     f"LOGS:\n{logs}"
# )
#
# for log in logs:
# iter_logs = iter(logs)
# print(next(iter_logs))
# print(next(iter_logs))
# print(next(iter_logs))
# print(next(iter_logs))
# print(next(iter_logs))
# print(next(iter_logs))

# def read_file():
#     with open(file_path, 'r') as file:
#         for line in file.readlines():
#             yield line
#
# for l in read_file():
#     assert 'ERROR' not in l, (
#         "Errors in log",
#         f"Line:\n{l}"
#     )

# a = [10, 11, 12]
# for i in range(len(a)):
#     print(i)
#
# """
# map(function, collection)
# """
# numbers = ['1', '2', '3']
# result = map(int, numbers)
# print(list(result))

# with open('11_users_ids.txt', 'r') as f:
#     user_ids = f.readlines()
#
# user_ids =  list(map(int, user_ids))
#
# print(user_ids)

# with open('11_prices.txt', 'r') as f:
#     prices = f.readlines()
#
# prices = list(map(int, prices))
# new_prices = list(map(lambda price: int(price * 1.1), prices))
#
# with open('11_new_prices.txt', 'w') as f:
#     for new_prices in new_prices:
#         f.write(str(new_prices) + '\n')

# print(new_prices)

# emails = ["ivan@example.com", "igor@example.com", "sam@example.com", "john@example.com"]
# access = [True, False, True, True]
#
# result = dict(zip(emails, access))
# print(result)

# numbers = ["1", "2", "3"]
# result = list(map(int, numbers))
#
# result_2 = [int(number) for number in numbers]


# import datetime
#
# now = datetime.datetime.now()
# print(datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
# print(now - datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
#
# created_at = datetime.datetime.now()
# expires_at = created_at + datetime.timedelta(minutes=7)
#
# print(created_at)
# print(expires_at)


# try:
#     file = open("11_new_prices.txt", 'r')
#     delta = file.read()
# except FileNotFoundError as err:
#     with open(file_path, 'a') as f:
#         f.write(f"\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ERROR Read {err}")
#     print(f"Read error: {err}")
# else:
#     print(f"File read success")
# finally:
#     file.close()

response = {'status': "ERROR"}

def parse_status(response):
    try:
        status = int(response['status'])
    except (KeyError, ValueError) as err:
        print(f"Error response: {response}")
        raise err
    else:
        return status
    finally:
        print("Parsing status success")

status = parse_status(response)
print(status)