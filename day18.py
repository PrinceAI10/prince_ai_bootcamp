# SET LESSONS (GUIDED EXAMPLES)

# CREATE SET
cities = {"Kumasi", "Accra", "Tamale", "Cape Coast", "Takoradi"}
print(cities)

# ADD ITEMS
languages = set()
languages.add("Twi")
languages.add("English")
languages.add("Ga")
print(languages)

#3 ADD ITEM TWICE
languages = {"Twi", "English", "Ga"}
languages.add("Twi")
print(languages)

#4 REMOVE ITEM
languages = {"Twi", "English", "Ga"}
languages.remove("English")
print(languages)
#Remove crashes when item does not exit, hence let use 'discard' to remove safely.
languages.discard("Dutch")

#5 CHECK ITEM MEMBERSHIP
languages = {"Twi", "English", "Ga"}
if "Twi" in languages:
    print("Twi is in the set.")
else:
    print("Twi not found.")

#6 LOOP THROUGH A SET
fruits = {"mango", "orange", "pawpaw", "banana"}
for fruit in fruits:
    print(f"I like {fruit}")

# CONVERT LIST TO SET (GET UNIQUE VALUES)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4]
unique_values = set(numbers)
print(unique_values)
print(len(unique_values))

# SET OPERATIONS (UNION, INTERSECTION, DIFFERENCE)
mtn = {"024", "054", "055", "059"}
vodafone = {"020", "050"}
all_items = mtn.union(vodafone)
print(all_items)

common_items = mtn.intersection(vodafone)
print(common_items)

only_mtn = mtn.difference(vodafone)
print(only_mtn)

# COUNTING UNIQUE WORDS IN SENTENCES
sentence = "the dog and the cat and the bird"
words = sentence.split()
unique_words = set(words)
print(unique_words)
print(len(unique_words))

# COMMON ELEMENTS BETWEEN TWO LISTS
cs_class = [101, 102, 103, 104, 105]
math_class = [103, 105, 106, 107]
cs_set = set(cs_class)
math_set = set(math_class)
common_elements = cs_set.intersection(math_set)
print(common_elements)
                        
