# Coding Exercise No.15
# Dice Rolling Simulator

import random

roll_again = "Y"
while roll_again == "Y":
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    print(f"Dice1: {dice1}", f"\nDice2: {dice2}")
    roll_again = input("Roll the dice again? (Y/N) ")
    