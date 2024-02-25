# A class is like a blueprint for creating objects. An object has properties and methods
# (functions) associated with it. Almost everything in Python is an object.

# Create Class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.email = email
        self.name = name
        self.age = age

    # Method
    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend class

class Customer(User):
    def __init__(self, name, email, age):
        self.email = email
        self.name = name
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and i am {self.age} and my balance is {self.balance}'


# Init user object
user1 = User('john', 'john@class.com', 45)

# Init customer object
susan = Customer('Susan', 'Susan@class.com', 25)


susan.set_balance(500)
print(susan.greeting())


user1.has_birthday()
print(user1.greeting())

# print(user1.name) # john
# print(type(user1)) # <class '__main__.User'>