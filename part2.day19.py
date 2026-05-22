def analyze_load_shedding(accra, kumasi, all_hours):
    result = {
        "both_dark": accra & kumasi,
        "only_accra_dark": accra - kumasi,
        "only_kumasi_dark": kumasi - accra,
        "at_least_one_dark": accra|kumasi,
        "both_have_power": all_hours - (accra|kumasi)
    }
    return result