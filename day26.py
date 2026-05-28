# DAY 26 (STRING MANIPULATION)
# REVERSE STRING (PATTERN = SLICE BACKWARDS)
def reverse_string(text):
    return text[::-1]

# IS PALINDROME (PATTERN = COMPARE WITH REVERSE)
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False
    
# COUNT CHARACTERS (PATTERN = LEN ON STRING)
def count_chars(word):
    return len(word)

# FIRST CHARACTER (PATTERN = INDEX 0)
def first_char(word):
    return word[0] if word else ""

# LAST CHARACTER (PATTERN = INDEX -1)
def last_char(word):
    return word[-1] if word else ""