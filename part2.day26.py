# STRING MANIPULATION PART 2
# FIRST 3 CHARACTERS (PATTERN = SLICE START TO INDEX)
def first_three(word):
    return word[:3] if word else ""

# LAST 3 CHARACTERS (PATTERN = SLICE FROM NEGATIVE)
def last_three(word):
    return word[-3:] if word else ""

# SKIP EVERY OTHER CHARACTER (PATTERN = SLICE WITH STEP)
def skip_chars(word):
    return word[::2] if word else ""
    
# REMOVE FIRST AND LAST (PATTERN = SLICE MIDDLE)
def remove_first_last(word):
    return word[1:-1] if word else ""

# UPPERCASE (PATTERN = STRING METHOD .upper())
def uppercase(word):
    return word.upper()

# LOWERCASE (PATTERN = STRING METHOD .lower())
def lowercase(word):
    return word.lower()

# CAPITALIZE FIRST LETTER (PATTERN = STRING METHOD .capitalize())
def capitalize_first(word):
    return word.capitalize()

# TITLE CASE (PATTERN = STRING METHOD .title())
def title_case(word):
    return word.title()

# REPLACE WORD (PATTERN = STRING METHOD .replace())
def replace_word(word, old, new):
    return word.replace(old, new)

# COUNT OCCURRENCE (PATTERN = STRING METHOD .count())
def count(word, letter):
    return word.count(letter)