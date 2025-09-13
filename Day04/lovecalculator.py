#!/bin/python3
# TRUE LOVE in names
# Ask for two names, calculate a "love score" based on the letters in "TRUE" and "LOVE"

name1 = input("What is your name? ").lower().replace(" ", "")
name2 = input("What is your crush's name? ").lower().replace(" ", "")

combined = name1 + name2
true_count = sum(combined.count(letter) for letter in "true")
love_count = sum(combined.count(letter) for letter in "love")

score = int(f"{true_count}{love_count}")

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")