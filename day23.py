# REVISION (DAY 1 TO DATE)

# EVEN OR ODD (PATTERN = CONDITIONAL RETURN)
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# POSITIVE, NEGATIVE OR ZERO (PATTERN = CONDITIONAL LADDER)
def check_number(num):
    if num > 0:
        return "Positive" 
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
    
# CAN VOTE (PATTERN = CONDITIONAL THRESHOLD)
def can_vote(num):
    if num >= 18:
        return "Eligible"
    else:
        return "Ineligible"
    
# GRADE CALCULATOR (PATTERN = GRADE RETURN LADDER)
def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

# FIZZBUZZ (PATTERN = CONDITIONAL LADDER WITH MODULO)
def fizzbuzz(n):
    if n % 15 == 0:
        return "Fizzbuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
    
# MAX OF TWO (PATTERN = COMPARISON RETURN)
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
    
# MAX OF THREE (PATTERN = NESTED COMPARISON)
def max_of_three(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
    
# IS LEAP YEAR? (PATTERN = NESTED CONDITIONALS)
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
# TICKET PRICE BY AGE (PATTERN = CONDITIONAL LADDER)
def ticket_price(age):
    if age < 5:
        return 0
    elif age < 18:
        return 10
    elif age >= 65:
        return 7
    else:
        return 15
    
# BMI CATEGORY (PATTERN = CONDITIONAL LADDER)
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

    