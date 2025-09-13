#!/bin/python3
# 📝 Pizza Order Calculator
# Ask the user for pizza size, pepperoni, and extra cheese, then calculate the final bill.
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L").casefold()
add_pepperoni = input("Do you want pepperoni? Y or N").casefold()
extra_cheese = input("Do you want extra cheese? Y or N").casefold()
size = str(size)
bill = 0
y = "y"
s = "s"
m = "m"
l = "l"

if size == s:
    bill = 15
elif size == m:
    bill = 20
elif size == l:
    bill = 25
else:
    print("You didn't used the correct form")

if add_pepperoni == y:
    if size == s:
        bill += 2
    else:
        bill += 3

if extra_cheese == y:
    bill += 1

print(bill)

