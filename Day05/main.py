#/bin/python3
# FizzBuzz Program
# ----------------
# Print numbers from 1 to 100 (inclusive).
#
# Rules:
# 1. If the number is divisible by 3 → print "Fizz".
# 2. If the number is divisible by 5 → print "Buzz".
# 3. If the number is divisible by both 3 and 5 → print "FizzBuzz".
# 4. Otherwise, print the number itself.

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)