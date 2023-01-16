"""
Create a program with a predefined dictionary for a person. Include the following information:
 name, gender, age, address and phone.

Ask the user what information he wants to know about the person (example:"name),
 then print the value associated to that key or display a message in case the key is not found.
"""

person = {"name": "Jhon Green", "gender": "Male", "age": "25", "address": "109 Panny Lane", "phone": "982733633"}

key = input("What information do you wont to know about a person? ").lower()
result = person.get(key, "That information is not available")
print(result)