#!/bin/python3
# This program calculates a user's Body Mass Index (BMI) based on their height and weight.
# It then categorizes the BMI into underweight, normal weight, slightly overweight, obese, or clinically obese.

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = round(weight / (height * height), 2)

if bmi < 18.5:
    print('Under 18.5 they are underweight')
elif bmi > 18.5 and bmi <= 25:
    print('Over 18.5 but below 25 they have a normal weight')
elif bmi > 25 and bmi < 30:
    print('Over 25 but below 30 they are slightly overweight')
elif bmi > 30 and bmi < 35:
    print('Over 30 but below 35 they are obese')
elif bmi > 35:
    print('Above 35 they are clinically obese.')