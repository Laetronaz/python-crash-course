# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create Class


class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extends classes


class Customer(User):
     # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'


# Init the user object
michel = User('Michel Pelland', 'michelpelland12@fakemail.com', 28)
# Init Customer object
bob = Customer('Bob', 'bob@fakemail.com', 22)
bob.set_balance(500)


michel.has_birthday()
print(michel.greeting())
print(bob.greeting())
