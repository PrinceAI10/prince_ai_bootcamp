# PART 2 OF DAY 29 (ERROR HANDLING (TRY/EXCEPT))

# SAFE LIST CONVERTER
def safe_list_convert(text):
    try:
        words = text.split(",")
        numbers = []
        for word in words:
            num = int(word)
            numbers.append(num)
        return numbers
    except ValueError:
        return "Invalid number in the list."
    
# DICTIONARY WITH DEFAULT
def get_or_default(dictionary, key, default):
    try:
        return dictionary[key]
    except KeyError:
        return default
    
# FILE LINE COUNTER
def file_line_count(filename):
    try:
        with open(filename, "r") as file:
            content = file.readlines()
            count = 0
            for line in content:
                count += 1
        return count
    except FileNotFoundError:
        return -1

# TYPE CHECKER
def can_be_converted(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
    
# SAFE AVERAGE
def safe_average(numbers):
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return "List is empty"
    except TypeError:
        return "List contains non-numbers"
    
# CHAINED EXCCEPTIONS
def read_first_line(filename):
    try:
        with open(filename, "r") as file:
            content = file.readline()
            return int(content)
    except FileNotFoundError:
        return "filename not found."
    except ValueError:
        return "Line contains a non-number."
    
# RAISE WITH MESSAGE
def validate_name(name):
    if name == "":
            raise ValueError("No name found.")
    return name
    
# MULTIPLE INPUT RETRY
def enter_number():
    for _ in range(3):
        try:
            return int(input("Enter number: "))
        except ValueError:
            print("Try again.")
    return None

# SAFE FILE WRITE
def write_file(filename):
    try:
        with open(filename, "w") as file:
            file.write("Hello World!\n")
        return True
    except OSError:
        print("filename not found.") 
    return False
    
# def validate_po