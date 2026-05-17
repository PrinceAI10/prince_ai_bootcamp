# TRIAL QUESTIONS
def get_parking_fee(hours):
    if hours <= 1:
        return 3
    elif hours <= 3:
        return 5
    elif hours <= 6:
        return 10
    elif hours <= 24:
        return 20

def get_loan_eligibility(credit_score):
    if credit_score < 500:
        return "Denied"
    elif credit_score < 650:
        return "High interest"
    elif credit_score < 750:
        return "Standard"
    else:
        return "Premium"
    
def get_game_rank(wins):
    if wins <= 5:
        return "Bronze"
    elif wins <= 15:
        return "Silver"
    elif wins <= 30:
        return "Gold"
    elif wins <= 50:
        return "Platinum"
    else:
        return "Diamond"
    
def get_travel_advice(country):
    if country == "Accra":
        return "Capital. Traffic heavy."
    elif country == "Kumasi":
        return "Garden City. Kejetia Market."
    elif country == "Tamale":
        return "Northern Region. Hot climate."
    elif country == "Cape Coast":
        return "Historic. Castles."
    else:
        return "Explore Ghana!"
    
def get_scholarship_tier(gpa,sat):
    if gpa >= 3.8 and sat >= 1400:
        return "Full Ride."
    elif gpa >= 3.5 and sat >= 1300:
        return "Half Tuition."
    elif gpa >= 3.0 and sat >= 1200:
        return "Partial Tuition."
    else:
        return "Not Eligible."
    
# CHALLENGE
def get_load_shedding_status(time, area):
    if area == "Industrial":
        return "No shedding. Critical Infrastructure."
    elif area == "Commercial" and 18 <= time <= 22:
        return "Shedding active. Peak hours."
    elif area == "Commercial":
        return "No shedding. Off peak."
    elif area == "Residential" and ((0 <= time <= 5) or (18 <= time <= 23)):
        return "Shedding active. High demand."
    elif area == "Residential" and 6 <= time <= 17:
        return "No shedding. Low demand."
    else: 
        return "Unknown Area."

print(get_load_shedding_status(20, "Industrial"))
print(get_load_shedding_status(19, "Commercial"))
print(get_load_shedding_status(10, "Commercial"))
print(get_load_shedding_status(22, "Residential"))
print(get_load_shedding_status(12, "Residential"))
print(get_load_shedding_status(8, "School"))



    