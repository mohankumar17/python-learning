from healthpackage.calories import get_calories_per_day
from healthpackage.bmi import get_bmi

print(get_bmi(height_in_cm=182, weight_in_kg=82))

print(get_calories_per_day(height_in_cm=182, weight_in_kg=82, age=24, gender="m"))
print(get_calories_per_day(height_in_cm=182, weight_in_kg=82, age=24, gender="f"))