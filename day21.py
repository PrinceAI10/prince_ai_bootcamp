# TRIAL QUESTIONS
# EXAMPLE 1 (PRINTING SQUARE GRID)
def print_grid(n):
    for i in range(n):
        print('#' * n)

# EXAMPLE 2 
def sum_all_pairs(numbers):
    total = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            total += numbers[i] + numbers[j]
    return total 
print(sum_all_pairs([1, 2, 3, 4]))

# EXAMPLE 3
def countdown(n):
    while n >= 1:
        print(n)
        n = n - 1
    print("Blast off! ")

# EXAMPLE 4
def multiplcation_table(n):
    for i in range(1, n + 1):
        for j in range(1, n+1):
            print(i * j, end="")
        print()

# EXAMPLE 5
def guess_password(correct, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        guess = input("Enter password: ")
        if guess == correct:
            print("Access granted! ")
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print("Wrong password. {remaining} attempts left. ")
    print("Access denied. Too many failed attempts.")