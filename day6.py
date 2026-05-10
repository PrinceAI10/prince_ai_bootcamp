citizenship = input("Are you a ghanaian? (yes/no):" )
if citizenship == "no":
    print("You must be a ghanaian to vote in Ghana." )
else:
    age = int(input("How old are you?" ))
    remainder = 18 - age
    if age<18:
        print(f"You are a ghanaian but too young to vote. Wait for {remainder} more years")
    else:
        disqualification = input("Are you a disqualified candidate? (yes/no)" )
        if disqualification == "yes":
            print("You are currently disqualified from voting." )
        else:
            print("You are eligible to vote for the President of Ghana." )
