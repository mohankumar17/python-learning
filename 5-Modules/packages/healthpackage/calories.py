def get_calories_per_day(height_in_cm, weight_in_kg, age, gender):
    bmr = (10 * weight_in_kg) + (5.25 * height_in_cm) - (5 * age)
    if gender == "m":
        return bmr + 5
    else:
        return bmr - 161
