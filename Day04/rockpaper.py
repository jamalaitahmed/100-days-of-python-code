# 📝 Rock, Paper, Scissors Game
# Let the user choose Rock, Paper, or Scissors, randomly select the computer's choice, 
# display both choices with ASCII art, and determine the winner.

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Question = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
Q1 = int(Question)
if Q1 > 2:
    print("Error")

computer = int(random.randint(0, 2))
if computer == 1:
    print(f"Computer kiest Paper {computer}" + f"{paper}")
elif computer == 0:
    print(f"Computer kiest Rock {computer}" + f"{rock}")
elif computer == 2:
    print(f"Computer kiest Scissors {computer}" + f"{scissors}")

if Q1 == 1:
    print(f"Jij kiest Paper {Q1}" + f"{paper}")
elif Q1 == 0:
    print(f"Jij kiest Rock {Q1}" + f"{rock}")
elif Q1 == 2:
    print(f"Jij kiest Scissors {Q1}" + f"{scissors}")

if Q1 == computer:
    print("Draw!")
if Q1 == 0 and computer == 2:
    print("You win!")
elif Q1 == 2 and computer == 0:
    print("You Lose!")
elif Q1 > computer:
    print("You win!")
elif computer > Q1:
    print("You lose!")

