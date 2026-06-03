# DAY 32 (ENCAPSULATION AND PROPERTIES)

# Q1 = PROTECTED ATTRIBUTE
class BankAccount:
    def __init__(self):
        self._balance = 0
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
    def get_balance(self):
        return self._balance
    
# Q2 = PRIVATE ATTRIBUTE WITH __
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def get_balance(self):
        return self.__balance

# Q3 = @PROPERTY FOR READ-ONLY
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
# Q4 = @PROPERTY WITH SETTER
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

# Q5 = PROTECTED METHOD
class Student:
    def __init__(self, name, score):
        self.name = name
        self._score = score
    def _calculate_grade(self):
        if self._score >= 80:
            return "A"
        return "B"
    def report(self):
        return f"{self.name}: {self._calculate_grade()}"
    
# Q6 = GETTER WITHOUT SETTER (READ-ONLY)
class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.name = name
    @property
    def user_id(self):
        return self.__user_id
    
# Q7 = VALIDATION IN SETTER
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age 
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

# Q8 = COMPUTED PROPERTY
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
# Q9 = LAZY PROPERTY (CACHED)
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
    @property
    def area(self):
        if self._area is None:
            self._area = 3.14 * self.radius ** 2
        return self._area
    
# Q10 = ENCAPSULATED STUDENT GRADE
class Student:
    def __init__(self, name):
        self.name = name
        self.__score = 0
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("Score must be 0-100")
     
    @property
    def grade(self):
        if self.__score >= 80:
            return "A"
        elif self.__score >= 70:
            return "B"
        elif self.__score >= 60:
            return "C"
        else:
            return "F"



    
