# DAY 31 (INHERITANCE)

# Q1 = BASIC INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
# Q2 = USING super().init
class Animal:
    def __init__(self, name):
        self.name = name
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

# Q3 = METHOD OVERRIDE
class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
# Q4 = ADDING NEW METHODS
class Animal:
    def __init__(self, name):
        self.name = name
class Bird(Animal):
    def fly(self):
        return f"{self.name} is flying!"
    
# Q5 = MULTILEVEL INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name
class Mammal(Animal):
    def feed_milk(self):
        return "Feeding milk"
class Dog(Mammal):
    def speak(self):
        return "Woof!"
    
# Q6 = isinstance() CHECK
class Animal:
    pass
class Dog(Animal):
    pass
d = Dog()
print(isinstance(d, Dog))     
print(isinstance(d, Animal))

# Q7 = BANK ACCOUNT INHERITANCE
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        self.balance += self.balance * rate

# Q8 = VEHICLE HIERARCHY
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
class Car(Vehicle):
    def drive(self):
        return "Driving"
class ElectricCar(Car):
    def charge(self):
        return "Charging"
    
# Q9 = SHAPE WITH AREA
class Shape:
    def area(self):
        return 0
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
# Q10 = STUDENT ---- GRADUATE STUDENT
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis):
        super().__init__(name, student_id)
        self.thesis = thesis