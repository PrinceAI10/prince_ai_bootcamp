# FILE I/O PART 2
# EXAMPLES SET 2

# APPEND TO FILE (PATTERN = APPEND MODE)
def add_name():
    with open("name.txt", "a") as file:
        file.write("Yaw\n")

# WRITE LIST TO FILE (PATTERN = 'for' LOOP + WRITE)
def write_list(filename, items):
    with open(filename, "w") as file:
        for item in items:
            file.write(item + "\n")
    
# FIND WORD IN FILE (PATTERN = READ + MEMBERSHIP)
def find_word(filename, word):
    with open(filename, "r") as file:
        content = file.read()
        return word in content
    
# COPY FILE (PATTERN = READ SOURCE, WRITE DESTINATION)
def copy_file(source, destination):
    with open(source, "r") as src:
        content = src.read()
    with open(destination, "w") as dest:
        dest.write(content)
    
# COUNT WORDS IN FILE (PATTERN = READ + SPLIT + LEN)
def count_words_in_file(filename):
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
    return len(words)