# DAY 30 = OOP BASICS (CLASSES & OBJECTS)

# CREATE A CLASS
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# CREATE AN OBJECT
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.name)

# CLASS WITH METHOD
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return "Woof!"
    
# CLASS WITH STR
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Dog: {self.name}"
    
# BANK ACCOUNT
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    
# STUDENT WITH GRADE METHOD
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B"
        elif self.score >= 60:
            return "C"
        else:
            return "F"
        
# RECTANGLE
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
# COUNTER
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def get_count(self):
        return self.count

# BOOK
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_read = False
    def mark_read(self):
        self.is_read = True

# TEMPERATURE
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32