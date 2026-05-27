# REVISION 2 
# LOOPS AND LISTS

# PRINT 1 TO N (PATTERN = 'for' Loop range)
def print_1_to_n(n):
    for i in range(1, n+1):
        print(i)

# SUM 1 TO N (PATTERN = ACCUMULATOR)
def sum_1_to_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total
    
# SUM OF LIST (PATTERN = LIST ACCUMULATOR)
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# COUNT EVEN NUMBERS (PATTERN = CONDITIONAL COUNTER)
def count_even(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

# FIND MAXIMUM (PATTERN = TRACK BEST)
def find_max(nums):
    best = nums[0]
    for num in nums:
        if num > best:
            best = num
    return best

# FIND MINIMUM (PATTERN = TRACK BEST)
def find_min(nums):
    best = nums[0]
    for num in nums:
        if num < best:
            best = num
    return best

# COUNT OCCURRENCES (PATTERN = FREQUENCY COUNT)
def count_occurrences(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

# FILTER EVEN NUMBERS (PATTERN = FILTER TO NEW LIST)
def filter_even_numbers(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

# DOUBLE EACH NUMBER (PATTERN = TRANSFORM TO NEW LIST)
def double_each_number(nums):
    result = []
    for num in nums:
        result.append(num * 2)
    return result

# IS ITEM IN LIST? (PATTERN = LINEAR SEARCH)
def is_item_in_list(items, target):
    for item in items:
        if item == target:
            return True
    return False