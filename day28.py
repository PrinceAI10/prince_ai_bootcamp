# FILE I/0
# EXAMPLES

# WRITE TO A FILE
def write_greeting():
    with open("greeting.txt", "w") as file:
        file.write("Hello, Ghana!")

# READ ENTIRE FILE
def read_greeting():
    with open("greeting.txt", "r") as file:
        return file.read()

# WRITE MULTIPLE LINES
def write_lines():
    with open("greeting.txt", "w") as file:
        file.write("Prince\n")
        file.write("Owusu\n")
        file.write("Afriyie\n")

# READ LINES INTO LIST
def read_names():
    with open("greeting.txt", "r") as file:
        return file.readlines()
    
# COUNT LINES
def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())


