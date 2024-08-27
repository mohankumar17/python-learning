def get_bmi(height_in_cm, weight_in_kg):
    height_in_m= height_in_cm / 100
    return weight_in_kg/(height_in_m ** 2)
