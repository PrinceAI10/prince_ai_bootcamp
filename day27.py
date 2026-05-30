# STRING ACTIVE RECALL

def count_a(word):
    return word.count("a")

def is_ghana_phone(number):
    if number.startswith("0"):
        return True
    return False

def remove_vowels(word):
    result = ""
    for letter in word:
        if letter not in "aeiouAEIOU":
            result += letter
    return result

def abbreviation(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        proper = word.capitalize()
        result += proper[:1]
    return result

def reverse_words(sentence):
    sentence_1 = sentence.split()
    return " ".join(sentence_1[::-1])
    
   
        


            
