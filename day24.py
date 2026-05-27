# REVISION
# LOOPS AND LIST CONT'D

# FIRST EVEN NUMBER (PATTERN = EARLY EXIT SEARCH)
def first_even(nums):
    for num in nums:
        if num % 2 == 0:
            return num
    return None

# REVERSE LIST (PATTERN = BUILD BACKWARDS IN A LIST)
def reverse_list(items):
    result = []
    for i in range(len(items) - 1, -1, -1):
        result.append(items[i])
    return result

# SUM OF EVEN NUMBERS (PATTERN = ACCUMULATOR)
def sum_even_numbers(nums):
    total = 0
    for num in nums:
        if num % 2 == 0:
            total += num
    return total

# PRINT EACH ITEM (PATTERN = 'for' EACH LOOP)
def print_each(items):
    for item in items:
        print(item)

# COUNTDOWN WITH WHILE (PATTERN = WHILE COUNTER)
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")

# SUM UNTIL ZERO (PATTERN = WHILE SENTINEL)
def sum_until_zero(nums):
    total = 0
    while True:
        num = int(input("Enter number ( or 0 to stop): "))
        if num == 0:
            break
        total += num
    return total 

# ALL POSITIVE (PATTERN = ALL CHECK)
def all_positive(nums):
    for num in nums:
        if num <= 0:
            return False
    return True

# ANY NEGATIVE (PATTERN = ANY CHECK)
def any_check(nums):
    for num in nums:
        if num < 0:
            return True
    return False

# MULTIPLY ALL (PATTERN = ACCUMULATOR (MULTIPLICATION))
def multiply_all(nums):
    product = 1
    for num in nums:
        product *= num
    return product

# RANGE OF LIST (PATTERN = MAX - MIN)
def range_of_list(nums):
    return max(nums) - min(nums)
        
    
    