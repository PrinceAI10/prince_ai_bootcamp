grades = []
for i in range(5):
    grade = float(input(f"Give me your top Physics grade {i+1} from high school: "))
    grades.append(grade)
total = 0
for grade in grades:
    total = total + grade
count = len(grades)
average = total/count
if average>=80:
    letter = "A"
elif average>=70:
    letter = "B"
elif average>=60:
    letter = "C"
elif average>=50:
    letter = "D"
else:
    letter = "F"
print(f"Your grade is {average}. Your grade letter is {letter}. ")




    




    