# TRIAL QUESTION 1
capitals = {
    "Ghana": "Accra",
    "Nigeria": "Abuja",
    "Kenya": "Nairobi",
    "USA": "Washington D.C"
}

def get_capital(country):
    if country in capitals:
        return capitals[country]
    else:
        return "Not in database."
    

