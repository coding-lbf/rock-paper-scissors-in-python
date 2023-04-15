# Create a Rock, Paper, Scissors Game with Python

# Import necessary modules
import random

# Define the main function
def main():
    # Print welcome message
    print("Welcome to the Rock, Paper, Scissors Game!")
    
    # Ask user for input
    user_input = input("Please enter your choice (Rock, Paper, Scissors): ")
    
    # Check user input
    if user_input == "Rock":
        play_game(user_input)
    elif user_input == "Paper":
        play_game(user_input)
    elif user_input == "Scissors":
        play_game(user_input)
    else:
        print("Invalid input. Please try again.")
        main()
        
# Define the play_game function
def play_game(user_choice):
    # Generate computer's choice
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Compare user's choice and computer's choice
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "Rock" and computer_choice == "Paper":
        print("Computer wins!")
    elif user_choice == "Rock" and computer_choice == "Scissors":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("You win!")
    elif user_choice == "Paper" and computer_choice == "Scissors":
        print("Computer wins!")
    elif user_choice == "Scissors" and computer_choice == "Rock":
        print("Computer wins!")
    elif user_choice == "Scissors" and computer_choice == "Paper":
        print("You win!")
    
    # Return to main menu
    main()
    
# Call the main function
if __name__ == "__main__":
    main()
