# ERROR HANDLING (TRY/EXCEPT/FINALLY)
# EXAMPLE QUESTIONS

# SAFE INTEGER INPUT
def safe_int():
    try:
        number = int(input("Enter a number: "))
        return number
    except ValueError:
        return "Not a number."

# SAFE DIVISION
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."
    
# FILE READER
def file_reader(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File Not Found."
    
# DICTIONARY LOOKUP
def get_value(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return "Key Not Found."
    
# LIST INDEX
def list_index(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index Out Of Range."

# MULTIPLE EXCEPTIONS
def calculate(value):
    try:
        num = int(value)
        fixed_rate = 100 / num
        return fixed_rate
    except ValueError:
        return "Not a number."
    except ZeroDivisionError:
        return "Cannot divide by zero."
    
# FINALLY BLOCK
def open_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File Not Found."
    finally:
        print("Operation complete.")

# RAISE YOUR OWN ERROR
def raise_error(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

# TRY/EXCEPT IN LOOP
def get_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter number (or 0 to stop): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("It's not a number.")
    return numbers

# NESTED TRY
def load_config(filename):
    try:
        with open(filename, "r") as file:
            try:
                content = int(file.read())
                return content
            except ValueError:
                return "Config is not a number."
    except FileNotFoundError:
        return "Config file not found."







 
