# Guess the Number

import math
import random

lower = int(input("Enter lower bond: "))
upper = int(input("Enter upper bond: "))
number_of_chances = int(math.log(upper-lower+1,2))
print(f"\n\tYou have only {number_of_chances} chances to guess the integer!\n")

generated_number = random.randint(lower, upper)

count = 0

guessed_correctly = False

while count < number_of_chances:
    count += 1
    guess = int(input("Guess the number: "))
    if guess == generated_number:
        print(f"Congratulations! You did it in {count} try/tries")
        guessed_correctly = True
        break
    elif guess > generated_number:
        print("You guessed too high!")
    elif guess < generated_number:
        print("You guessed too low!")

if not guessed_correctly:
    print(f"\nThe number is {generated_number}")
    print("\tBetter luck next time!")



