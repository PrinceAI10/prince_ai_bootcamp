secret = 7
number = int(input("Guess my secret number: "))
while number!= secret:
    if number>secret:
        print("Too high, please try again. ")
        number = int(input("Try again: "))
    elif number<secret:
        print("Too low, please try again. ")
        number = int(input("Try again: "))
print("You have done it!, such a genius. The secret number is 7 ")       


 