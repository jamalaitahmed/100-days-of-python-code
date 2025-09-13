#!/bin/python3
'''
Tip Calculator
Write a program that splits a bill between multiple people, including a tip.

- Ask the user for the total bill amount (e.g., 124.56).
- Ask what percentage tip they would like to give (e.g., 10, 12, or 15).
- Ask how many people will split the bill.
- Calculate the total bill including the tip.
- Divide the total by the number of people.

Display how much each person should pay, rounded to 2 decimal places.
'''
bill = input("Welcome to the tip calculator!\nWhat was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
total_bill = float(bill) * (1 + int(tip) / 100)
split_bill = total_bill / int(people)
print(f"Each person should pay: ${round(split_bill, 2)}")
