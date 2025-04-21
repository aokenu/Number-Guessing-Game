import random

import art
print(art.logo)

# Initializing the number of attempts
hard_attempts = 6
easy_attempts = 11

# Initializing the number of guess
player_guess = 0

# Function for the computer to pick a random number
def pick_a_number():
    random_number = random.choices(range(5, 101, 5))
    return random_number

player_pick = pick_a_number()

# Display the welcome text of the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Choosing the game's difficulty level
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard' :")

# Loop to repeat the guess until the player runs out of guess
while hard_attempts and easy_attempts > 0:
    if difficulty_level == 'easy':
        easy_attempts -= 1
        print(f"You have {easy_attempts} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
    elif difficulty_level == 'hard':
        hard_attempts -= 1
        print(f"You have {hard_attempts} attempts remaining to guess the number.")
        player_guess = int(input("Make a guess: "))
    else:
        print("Wrong choice! The choice does not exist")

    print(player_guess)
    #print(player_pick[0])

    # Function to check the player's guessed number against the computer's randomly picked number
    def compare_numbers():
        if player_guess > player_pick[0]:
            print("Too high.")
            print("Guess again.")
        elif player_guess < player_pick[0]:
            print("Too low.")
            print("Guess again.")
        else:
            print("Correct! You guessed the correct number")
            exit()

    compare_numbers()

# Display to ask the player to start the game all over when the game ends.
print("You've run out of guesses. Refresh the page to guess again.")
