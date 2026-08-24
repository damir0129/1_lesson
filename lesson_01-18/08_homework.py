users = [
    {"id": 101, "name": "Alice"},
    {"id": 102, "name": "Bob"},
    {"id": 103, "name": "Kate"}
]

users_id = [user["id"] for user in users]

print(users_id)


orders = [
    {"id": 1, "status": "created"},
    {"id": 2, "status": "paid"},
    {"id": 3, "status": "cancelled"},
    {"id": 4, "status": "paid"}
]

paid_orders = [order for order in orders if order["status"] == "paid"]
print(paid_orders)


response = {
    "orders": [
        {"items": ["apple", "banana"]},
        {"items": ["milk", "bread"]}
    ]
}

items_response = [item for order in response["orders"] for item in order["items"]]
print(items_response)


def log_test(func):
    def wrapper(*args, **kwargs):
        print("Start test")
        result = func(*args, **kwargs)
        print("End test")
        return result
    return wrapper

@log_test
def login_test():
    print("Login step")

login_test()


def test_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Running test: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished test: {func.__name__}")
        return result
    return wrapper

@test_logger
def test_create_user():
    print("Create user step")

test_create_user()


def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {' '.join(map(str, args))}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@log_args
def add(a, b):
    return a + b

add(2, 3)


users = {
    "users": [
        {
            "name": "admin",
            "age": 14,
            "id": 1,
            "is_admin": True
        },
        {
            "name": "Damir",
            "age": 22,
            "id": 2,
            "is_admin": True
        },
        {
            "name": "Ivan",
            "age": 18,
            "id": 3,
            "is_admin": False
        },
    ],
}

def check_user(func):
    def wrapper(*args, **kwargs):
        user = args[0] if args else kwargs.get["user"]
        if user and user.get("is_admin"):
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper

@check_user
def get_orders(name):
    print("Access Granted")

get_orders(users["users"][2])


def is_admin(func):
    def wrapper(user, *args, **kwargs):
        if not user["is_admin"]:
            print("Access Denied")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@is_admin
def get_orders(user):
    print(f"Orders list {user['name']}")

user1 = {"name": "Damir", "is_admin": True}
user2 = {"name": "Ivan", "is_admin": False}

get_orders(user1)
get_orders(user2)