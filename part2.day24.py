# 10 CHALLENEG QUESTIONS
def is_even(num):
    if num % 2 == 0:
        return True
    return False
    

def sum_odd(numbers):
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
    


def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiou":
            count += 1
    return count


def is_palindrome(word):
    if word == word[:: -1]:
        return True
    return False


def fahrenheit_to_celsius(f):
    c = (f - 32) * 5/9
    return c


def longest_word(words):
    best = words[0]
    for word in words:
        if len(word) > len(best):
            best = word
    return best

def remove_duplicates(items):
    items_new = set(items)
    return list(items_new)


def divisible_by(numbers, n):
    result = []
    for number in numbers:
        if number % n == 0:
            result.append(number)
    return result


def merge_alternate(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
    return result

def second_largest(numbers):
    first_largest = max(numbers)
    remaining = [num for num in numbers if num != first_largest]
    return max(remaining)




    




