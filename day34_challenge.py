# Day 34 — Quick Challenge
# Write a function that counts words in a sentence
# without using .split()

def count_words(sentence):
    count = 0
    in_word = False
    for char in sentence:
        if char != " " and not in_word:
            count += 1
            in_word = True
        elif char == " ":
            in_word = False
    return count