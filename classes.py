# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'

    def incrementAge(self):
        self.age+=1

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    
    def setBalance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and i am {self.age} and my balance is {self.balance}'
# Init a user object 
user1 = User('Charles', 'Charles@gmail.com',  37)
customer = Customer('John Doe', 'john@gmail.com', 29)
customer.setBalance(500)

user1.incrementAge()
print(customer.greeting())
print(user1.greeting())
