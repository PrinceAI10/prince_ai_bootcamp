# CHALLENGE VERSION (STRING MANIPULATION)

# FIND POSITION (PATTERN = STRING METHOD .find())
def find_position(word, letter):
    return word.find(letter)

# STARTS WITH (PATTERN = STRING METHOD .startswith())
def starts_with(word, prefix):
    return word.startswith(prefix)

# ENDS WITH (PATTERN = STRING METHOD .endswith())
def ends_with(word, suffix):
    return word.endswith(suffix)

# REMOVE WHITESPACE (PATTERN = STRING METHOD .strip())
def remove_both_ends(word):
    return word.strip()

# SPLIT INTO WORDS (PATTERN = STRING METHOD .split())
def split_words(sentence):
    return sentence.split()