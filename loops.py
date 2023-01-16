import random

"""
1. Create a program that asks the user for 8 names of people and store them in a list.
 When all the names have been given, pick a random one and print it.

2. Create a guess game with the names of the colors.
 At each round pick a random color from a list and let the user try to guess it.
 When he does it, ask if he wants to play again. Keep playing until the user types "no"
"""

people = []

for x in range(0, 8):
    person = input("Type the name of a person: ")
    people.append(person)

index = random.randint(0, 7)
random_person = people[index]
print("Random person is", random_person)

# =========================================================
colors = ["white", "black", "red", "green", "blue", "yellow", "purple", "grey"]

while True:
    color = colors[random.randint(0, len(colors) - 1)]
    guess = input("I'm thinking about a color, can you guess it? ")

    while True:
        if color == guess.lower():
            break
        else:
            guess = input("Nope. Try Again: ")
    print("You guessed it! I was thinking about", color)
    play_again = input("Let's play again? Type 'no' to quit.")
    if play_again.lower() == 'no':
        break
print("It's fun, thanks for playing!")
