"Task 1"

class User:
    def __init__(self, email):
        self.email = email

    def show_email(self):
        print("email: ", self.email)

user = User("test@vk.ru")
user.show_email()

"Task 2"

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(100)
account.deposit(50)
account.withdraw(20)

print(account.balance)

"Task 3"

class Cart:
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item):
        self.items.append(item)

    def total_items(self):
        return len(self.items)

cart = Cart()
cart.add_item("laptop")
cart.add_item("mouse")
print(cart.total_items())

"Task 4"

class BaseAPI:
    def request(self):
        print("Base request")

class UserAPI(BaseAPI):
    def request(self):
        print("User request")

api = UserAPI()
api.request()

"Task 5"

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class AdminUser(User):
    def __init__(self, email, password, role):
        super().__init__(email, password)
        self.role = role

admin = AdminUser("admin@vk.ru", "pass", "admin")

print(admin.email)
print(admin.password)
print(admin.role)