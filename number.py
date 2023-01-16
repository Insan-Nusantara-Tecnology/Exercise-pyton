"""
Create a program to calculate the area and circumference of a circle.Ask the user for the radius.

Area = Phi x r*2
Circumference = 2 x Phi x r

r = radius
"""

import math

radius = float(input("Type the radius of the circle: "))
area = math.pi * (radius**2)
circumeference = 2 * math.pi * radius

print("The area of the circle is", round(area, 2))
print("The circumeference of the circle is", round(circumeference, 2))
