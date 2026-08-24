# numbers = [1,2,3,4,5,6]
# print(numbers)
#
# data = [1, 'hello', 1.23, False]
# print(data)
#
# print(data[2])
# print(data[-1])
#
# data[0] = 100
# print(data)
# print(data[1][-1])

# numbers.append(7)
# print(numbers)
# numbers.remove(4)
# print(numbers)
# numbers.insert(3, 456)
# print(numbers)
# el = numbers.pop()
# print(el)
# print(numbers)
# numbers.extend([4, 5])
# print(numbers)

# for num in numbers:
#     print(num)
#
# for index, value in enumerate(numbers):
#     print("index: ", index, "value: ", value)
#
# sq = [x * x for x in range(1, 6, 2)]
# print(sq)
#
# ages = (4, 20, 35, 18)
# print(ages)
#
# ages_1 = (4, 20, 35, 18) + (90,)
# print(ages_1)
#
# user = {
#     "name" : "Damir",
#     "surname" : "Ignatev"
# }
# print(user["name"])
# # print(user.get("surname"))
# print(user.get("surname_2", "Attribute not found"))
#
# user['age'] = 36
# user['name'] = "Dam"
#
# print(user)
#
# for key in user:
#     print(key)
#
# for value in user.values():
#     print(value)
#
# for key, value in user.items():
#     print(f"{key}: ", value)

# response = {
#     'status': 'Completed',
#     'additionalInfo': {
#         'statuses': ['Completed', 'Error', 'Processing'],
#         'id': "jew32-fkqeow-iwq9qp-o23or"
#     },
#     'structure': 'Done'
# }
# print(response['status'])
# print(response['additionalInfo']['statuses'][-1])

# response = {
#     'objects': [
#         {
#             'status': 'Completed',
#             'additionalInfo': {
#                 'statuses': ['Completed', 'Error', 'Processing'],
#                 'id': "jew32-fkqeow-iwq9qp-o23or"
#             },
#             'structure': 'Done'
#         },
#         {
#             'status': 'Error',
#             'additionalInfo': {
#                 'statuses': ['Completed', 'Error', 'Processing'],
#                 'id': "faqr2-gqha1-fmp3r-peps1"
#             },
#             'structure': 'Done'
#         },
#         {
#             'status': 'Error',
#             'additionalInfo': {
#                 'statuses': ['Completed', 'Error', 'Processing'],
#                 'id': "qtwew-fqwf3-hwtob-bwtr5"
#             },
#             'structure': 'Done'
#         }
#     ]
# }
#
# ids_error = []
#
# for object in response['objects']:
#     if object['status'] == 'Error':
#         ids_error.append(object['additionalInfo']['id'])
#
# print(ids_error)

# d = dict()

# s = {1, 2, 4, 4}
# l = [1, 2, 3, 4, 4, 4]
# s = set(l)
# print(s)

"""
tuple (картеж)
сеты
словари
"""