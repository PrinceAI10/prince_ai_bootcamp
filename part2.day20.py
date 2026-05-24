# EXAMPLE 4 (WHILE LOOP WITH COUNTER)

count = 1
while count <= 5:
    print(count)
    count = count + 1

#  EXAMPLE 5 (WHILE LOOP WITH USER INPUT)
total = 0
while True:
    num = int(input("Enter any random number ( or 0 to stop): "))
    if num == 0:
        break
    total = total + num
    print(f"Total : {total}")

# EXAMPLE 6 (WHILE LOOP WITH ATTEMPT LIMITS)
password = "howard2030"
attempts = 0
while attempts < 3:
    random = input("Enter password: ")
    attempts = attempts + 1
    if random == password:
        print("Access granted! ")
        break
    else:
        print("Access denied. ")
