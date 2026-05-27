# ABSOLUTE VALUE (PATTERN = CONDITIONAL RETURN)
def absolute_value(n):
    if n >= 0:
        return n
    return -n

# LAST ELEMENT OF A LIST (PATTERN = INDEX ACCESS)
def last_element(items):
    return items[-1]

# IS DIVISIBLE BY (PATTERN = MODULO CHECK)
def is_divisible(number , n):
    if number % n == 0:
        return True
    return False

# FIRST AND LAST (PATTERN = INDEX ACCESS)
def first_last(items):
    return (items[0], items[-1])

# COUNT WORDS IN A SENTENCE (PATTERN = SPLIT + COUNT)
def count_words_sentence(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        count += 1
    return count

# UPPERCASE STRING (PATTERN = STRING METHOD)
def to_upper(word):
    return word.upper()

# AVERAGE OF LIST (PATTERN = ACCUMULATOR + LEN)
def avg_list(numbers):
    total = 0
    for num in numbers:
        total += num
    count = len(numbers)
    avg_list = total/count
    return avg_list

# IS EMPTY? (PATTERN = TRUTHNESS CHECK)
def is_empty(items):
    if len(items) == 0:
        return True
    return False

# BETWEEN 1 & 10 (PATTERN = RANGE CHECK)
def between_1_and_10(number):
    if 1 <= number <= 10:
        return True
    return False

# START WITH VOWEL? (PATTERN = STRING INDEX + MEMBERSHIP)
def start_vowel(word):
    if word[0] in "aeiou":
        return True
    return False

# MIDDLE ELEMENT (PATTERN = INDEX CALCULATION)
def midd_element(items):
    return items[len(items) // 2]

# POWER OF (PATTERN = MATH OPERATOR)
def power(base, exp):
    return base ** exp

# IS MULTIPLE OF 3 AND 5 (PATTERN = COMBINED MODULO)
def divisible_3_5(number):
    if number % 3 == 0 and number % 5 == 0:
        return True
    return False

# CONCATENATE STRING (PATTERN = STRING ADDITION)
def concatenate(a, b):
    return a + b

# LIST LENGTH (PATTERN = LEN)
def list_length(items):
    return len(items)