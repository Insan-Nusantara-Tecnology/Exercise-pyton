"""
Create a porgram that asks the user for a number of Kilometers, converts is to Miles and prints the result
1 Mile = 1.609344 Km
"""

km = float(input("Type the number of kilometers: "))
miles = km / 1.609344
print(km, "km =", round(miles, 4), "miles")