expenses = []
while True:
    exp = float(input("What are your expense amounts and type '0' to stop: "))
    if exp == 0:
        break
    else:
        expenses.append(exp)
count = len(expenses)
total = sum(expenses)
avg = total / count
high = max(expenses)
low = min(expenses)
if len(expenses)>0:
    print(f"Count: {count} ")
    print(f"Total: {total}")
    print(f"Average: {avg}")
    print(f"Max expenses: {high}")
    print(f"Low expenses: {low} ")
elif len(expenses) == 0:
    print("Math error ")
else:
    print("No expenses!")