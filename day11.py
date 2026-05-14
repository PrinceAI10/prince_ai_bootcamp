numbers = []
for i in range(6):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
even = 0
odd = 0
for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
print(f"Even numbers: {even} ")
print(f"Odd numbers: {odd} ")
