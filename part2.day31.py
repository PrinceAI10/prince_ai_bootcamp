# PART 2 OF DAY 31 (INHERITANCE)

# Q1 = PERSON --- EMPLOYEE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

# Q2 = APPLIANCE --- WASHING MACHINE
class Appliance:
    def __init__(self, brand):
        self.brand = brand
    def turn_on(self):
        return "Power on"
class WashingMachine(Appliance):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

# Q3 = MEDIA --- MOVIE --- DOCUMENTARY
class Media:
    def __init__(self, title):
        self.title = title
class Movie(Media):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director
class Documentary(Movie):
    def __init__(self, title, director, topic):
        super().__init__(title, director)
        self.topic = topic

# Q4 = OVERRIDE str IN CHILD
class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal: {self.name}"
class Dog(Animal):
    def __str__(self):
        return f"Dog: {self.name}"

# Q5 = CALL PARENT METHOD FROM CHILD 
class Animal:
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} then Woof!"
    
# Q6 = hasattr() CHECK
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
d = Dog("Buddy", "Golden")
print(hasattr(d, "breed"))   
print(hasattr(d, "age"))

# Q7 = MULTIPLE CHILDREN
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Bird(Animal):
    def speak(self):
        return "Chirp!"

# Q8 = OVERRIDE innit COMPLETELY
class Animal:
    def __init__(self, name):
        self.name = name
class WildAnimal(Animal):
    def __init__(self, species, habitat):
        self.species = species
        self.habitat = habitat

# Q9 = INHERITANCE WITH METHOD USING PARENT ATTRIBUTE
class Account:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
class CurrentAccount(Account):
    def get_info(self):
        return f"Account {self.account_number}: ${self.balance}"
    
# Q10 = issubclass() CHECK
class Animal:
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass
print(issubclass(Dog, Animal))    
print(issubclass(Cat, Animal))    
print(issubclass(Dog, Cat)) 


