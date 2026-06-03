# PART 2 OF DAY 30 (OOP BASICS = CLASS AND OBJECT)

# TODO LIST (PATTERN = CLASS WITH STATE CHANGE + _STR_)
class Todo:
    def __init__(self, task):
        self.task = task
        self.completed = False
    def complete(self):
        self.completed = True
    def __str__(self):
        status = "Done!" if self.completed else "Continue"
        return f"[{status}] {self.task}"

# CAR (PATTERN = CLASS WITH METHOD RUNNING STRING)
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        return "Engine started"
    
# CALCULATOR (PATTERN = CLASS WITH UTILITY METHODS (NO __init__  NEEDED))
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    
# PLAYLIST (PATTERN = CLASS WITH LIST ATTRIBUTE + METHODS)
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def play_all(self):
        for song in self.songs:
            print(f"Playing: {song}")

# MINI STUDENT TRACKER (PATTERN = CLASS WITH DICTIONARY ATTRIBUTE + CRUD METHODS)
class StudentTracker:
    def __init__(self):
        self.students = {}
    def add_student(self, name, grade):
        self.students[name] = grade
    def get_student(self, name):
        return self.students.get(name, "Not found")

