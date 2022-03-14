import sys
weight = float(input("Please enter weight (in pounds) "))
height = float(input("Please enter height (in inches) "))
bmi = round((703 * weight) / pow(height, 2))
print("Your body mann index (BMI) is: " + str(bmi))