"""
1. Create a program that asks the user for his first name, his middle name and his last name. Then print:
 "Your initials are ___"
2. Let's say your company has a product with this lot number: "037-00901-00027". 037 is the country code.
 00901 is the product code. 00027 is the batch number.
 Create a program to print:
 Country code: ___
 Product code: _____
 Batch number: _____
"""

first_name = input("What's your first name? ")
middle_name = input("What's your middle name? ")
last_name = input("What's your last name? ")

print("Your initials are", first_name[0], middle_name[0], last_name[0])

# ==============================================
lot_number = "037-00901-00027"
print("Country code:", lot_number[0:3])
print("Product code:", lot_number[4:9])
print("Batch number:", lot_number[10:])
