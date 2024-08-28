from healthpackage.calories import get_calories_per_day
from healthpackage.bmi import get_bmi

print(get_bmi(height_in_cm=182, weight_in_kg=77.5))

print(get_calories_per_day(height_in_cm=182, weight_in_kg=77.5, age=25, gender="m"))
print(get_calories_per_day(height_in_cm=182, weight_in_kg=77.5, age=25, gender="f"))