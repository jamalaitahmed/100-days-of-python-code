#!/bin/python3
"""
Treasure Island Game
Your mission is to find the treasure.
1. Ask the user to choose "left" or "right".
2. If "left", ask if they want to "swim" or "wait".
3. If "wait", ask which door they choose: "red", "blue", or "yellow".
4. Print "Game Over" if the user makes a wrong choice.
5. Print "You win!" if the user chooses correctly.
6. Use input() to get choices and make the game case-insensitive using .lower().
"""

print("Welcome to treasure island, your mission is to find the treasure")
print("Left or right?")
q1 = input().lower()

if q1 == "left":
    print("Ok! Swim or wait? ")
    q2 = input()
    q2 = q2.lower()
    if q2 == "swim":
        print("Game Over")
    elif q2 == "wait":
        print("which door? red, blue or yellow")
        q3 = input()
        q3 = q3.lower()
        if q3 == "yellow":
            print("You win!")
        else:
            print("Game over! :) ")
    else:
        print("Game Over")
else:
    print("Game Over")

