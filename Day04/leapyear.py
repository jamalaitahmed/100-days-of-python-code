# This program checks if a given year is a leap year.
# A leap year is divisible by 4, but years divisible by 100 are not leap years unless they are also divisible by 400.

year = int(input("Which year do you want to check?"))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("Leap")
else:
    print("Not a leap year")
