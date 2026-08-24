# age = 17
#
# if age >= 18: # False
#     print("Access")

# age = 30
#
# if age >= 18: # True
#     print("Access")
# else:
#     print("Deny")
#
# count = 5
#
# if count >= 10:
#     print("discount 20%")
# elif count >= 5:
#     print("discount 10%")
# else:
#     print("discount 0%")

# count = 5
# sum_basket = 10_000
# if count >= 5 and sum_basket >= 10_000:
#     print("discount 20%")
#
# is_user = False
#
# if not is_user:
#     print("discount 20%")

attrs = [1, "hello", 3.14, False]

# for attr in attrs:
#     print(attr)
#     attrs.remove(attr)
#
# for i in range(len(attrs)):
#     print(attrs[i])

# i = 1
#
# while i < 11:
#     print(i)
#     i += 1

# status = "Success"
# status_error = "Error"
#
# status_input = input("Status from service: ")
# while status != status_input:
#     if status_input == status_error:
#         break
#     status_input = input("Status from service: ")
# print("Status:", status_input)
#
# for attr in attrs:
#     if isinstance(attr, (int, float)) and not isinstance(attr, bool):
#         continue
#     print(attr)

response = {
    "user" : "Damir",
    "is_admin" : True,
}
interface = "create" if response["is_admin"] else "view"
print(interface)