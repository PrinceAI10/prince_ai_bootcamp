# 5 CHALLENGE QUESTIONS

# QUESTION 1
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def call(self, number):
        return f"Calling {number}..."
    
# QUESTION 2
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def circumference(self):
        return 2 * 3.14 * self.radius
    
# QUESTION 3
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def remove_task(self, task):
        self.tasks.remove(task)
    def list_tasks(self):
        return self.tasks
    
# QUESTION 4
class Password:
    def __init__(self, password):
        self.password = password
    def is_strong(self):
        has_digit = False
        has_upper = False
        for char in self.password:
            if char.isdigit():
                has_digit = True
            if char.isupper():
                has_upper = True
        return len(self.password) >= 8 and has_digit and has_upper
    def mask(self):
        return "*" * len(self.password)
    
# QUESTION 5
class GradeTracker:
    def __init__(self):
        self.grades = {}
    def add_grade(self, subject, score):
        self.grades[subject] = score
    def get_average(self):
        total = sum(self.grades.values())
        return total / len(self.grades)
    def get_highest_subject(self):
        highest_subject = max(self.grades, key=self.grades.get)
        return highest_subject


