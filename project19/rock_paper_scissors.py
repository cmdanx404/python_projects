import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"]) # random.choice is used to randomly select an element from a list

def get_user_choice():
    choice = input("\nChoose Rock, Paper, or Scissors: ").lower() # priming read
    while choice not in ["rock", "paper", "scissors"]: # start of while loop
        print("\n\tInvalid choice. Please choose again.\n")
        choice = input("Choose Rock, Paper, or Scissors: ").lower() # loop read
    return choice # end of loop

def determine_winner(user, computer):
    print(f"\tYou chose: {user}")
    print(f"\tComputer chose: {computer}")
    
    if user == computer:
        return "\tIt's a draw!\n"

# grouped conditions

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "\tYou win!"
    else:
        return "\tYou lose!"
    
# driver function / main controller

def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Start the game

def main():
    play_game()

if __name__ == "__main__":
    main()

# This ensures the game only runs if the file is executed directly
