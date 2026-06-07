# GENERAL PYTHON REVIEW
# COUNT VOWELS

def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in "aeiou":
            count += 1
    return count

# FIZZBUZZ
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n
    
# PALINDROME CHECK
def is_palindrome(s):
    return s == s[::-1]

# FIND MAX IN LIST
def find_max(nums):
    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
    return largest

# WORD FREQUENCY
def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

# SAFE DIVISION
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
# STUDENT CLASS
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def get_letter_grade(self):
        if self.grade >= 80:
            return "A"
        elif self.grade >= 70:
            return "B"
        elif self.grade >= 60:
            return "C"
        else:
            return "F"

# LIST COMPREHENSION
def get_evens(nums):
    return [num for num in nums if num % 2 == 0]

# READ FILE
def read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
    
# MERGE DICTS
def merge_dicts(d1, d2):
    merged = d1.copy()

    for key, value in d2.items():
        if key in merged:
            merged[key] = max(merged[key], value)
        else:
            merged[key] = value
    return merged
    