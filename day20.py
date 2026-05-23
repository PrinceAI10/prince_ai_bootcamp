# NESTED LOOPS & WHILE LOOP PATTERNS

# EXAMPLE 1 (PRINTING A 5 BY 5 MULTIPLICATION TABLE, THUS NESTED FOR)
for i in range(1,6):
    for j in range(1,6):
        print(f"{i} * {j} = {i*j}")
    print("---")


# EXAMPLE 2 (GRID PATTERN, THUS NESTED FOR WITH LISTS)
grid = [
    [1,2,3],
    [4,5,6]

]
for row in range(len(grid)):
    for col in range(len(grid[row])):
        print((row,col)) 


# EXAMPLE 3 (FINDING A PAIR THAT SUMS TO A TARGET, THUS NESTED LOOP + CONDITION)
def find_pair(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(i+1, len(numbers))):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None 
