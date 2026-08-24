users = [
    {"name": "Alice", "role": "user"},
    {"name": "Bob", "role": "user"},
    {"name": "Kate", "role": "admin"}
]

def has_admin():
    for user in users:
        if user["role"] == "admin":
            return True

    return False
print(has_admin())

orders = [
    {"id": 101, "status": "created"},
    {"id": 102, "status": "processing"},
    {"id": 103, "status": "paid"}
]

def find_paid_order(orders):
    for order in orders:
        if order["status"] == "paid":
            return order
    return None


print(find_paid_order(orders))


statuses = ["processing", "processing", "ready"]

def wait_until_ready(statuses):
    index = 0
    while index < len(statuses):
        if statuses[index] == "ready":
            return True
        index += 1

    return False

print(wait_until_ready(statuses))