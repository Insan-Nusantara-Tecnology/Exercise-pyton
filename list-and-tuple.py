"""
1. Creat a program that asks the userr for his birthday in the format "DD-MM-YYYY", Then print:
"Your were born in [month]"

2. Create a program with a predefined list of people. Ask the user for his name,
 add it to the end of the list and print the updated list.
"""

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

birthday = input("Type your birthday in the format DD-MM-YYYY: ")

index = int(birthday[3:5]) -1
bd_month = months[index]

print("Your were born in", bd_month)

# ================================================
people = ["Jhon", "Mary", "Peter"]
user = input("Type your name: ")
people.append(user)
print("Here's the list: ", people)