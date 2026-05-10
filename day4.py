age = int(input("How old are you? "))
if age>= 18:
    print("You are eligible to vote. ")
else:
    remainder = 18 - age
    print(f"You are not eligible to vote. Wait for {remainder} more years. ")
print("Democracy matters. Register when you can. ")
