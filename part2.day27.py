# STRING ACTIVE RECALL Q6-Q10

def is_valid_email(email):
    if "@" in email and email.endswith(".com"):
        return True
    return False


def swap_case(text):
    result = ""
    for letter in text:
        if letter.islower():
            result += letter.upper()
        else:
            result += letter.lower()
    return result


def is_strong_password(password):
    has_upper = False
    has_digit = False
    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
    return len(password) >= 8 and has_upper and has_digit


def count_words_starting_with(sentence, letter):
    count = 0
    words = sentence.split()
    for word in words:
        if word.startswith(letter):
            count += 1
    return count


def mask_phone(number):
    return "*******" + number[-3:]

        
        
    
    
