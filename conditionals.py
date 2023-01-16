"""
Create a program to calculate the BMI(Body Mass Index) of a person.
Ask the user for his height in Meter and his weight in Kg.

BMI = weeight / (height * height)
- Weight in Kg
- Height in Meters

Print the BMI and the classification.
- Less than or equal to 18.5: Underweight
- Greater than 18.5 or less than or equal to 24.9: Normal weight
- Greater than 24.9 or less than or equal to 29.9: Overweight
- Greater than or equal to 30: Obesity
"""

weight = float(input("Type your weight in Kg (ex. 70.5)= "))
height = float(input("Type your height in Meter (ex. 1.75)= "))

bmi = weight / (height * height)
print(bmi)
print("Your BMI is: ", round(bmi, 2))

if bmi <= 18.5:
    classification = "Underweight"
elif 18.5 < bmi <= 24.9:
    classification = "Normal weight"
elif 24.9 < bmi <= 29.9:
    classification = "Overweight"
else:
    classification = "Obesity"

print("The classification of your BMI is", classification)
