# TRIAL QUESTION 1
def unique_countries(countries_list):
    countries_set = set (countries_list)
    return (len(countries_set))

#2 TRIAL QUESTION 2
def common_languages(lang1, lang2):
    lang1_set = set(lang1)
    lang2_set = set(lang2)
    common = lang1 & lang2
    return common

# TRIAL QUESTION 3
def only_in_first(set1, set2):
    only_in_set1 = set1 - set2
    return only_in_set1

# TRIAL QUESTION 4
def has_duplicate(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        else:
            seen.add(item)
    return False

# TRIAL QUESTION 5
def word_frequencies(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] = freq[word] + 1
    print(f"Unique words: {len(freq)} ")
    return freq


            
        
    