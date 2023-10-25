# Name: Farhana Lima
# Purpose: Assignment on number guessing game.
# Properties to be fulfilled:
# Randomly choose a number between 1 and 100 (inclusive)
# Have the player enter a guess via input
# Tell the player the guess is high, low, or correct
# If high or low, allow the player to enter another guess
# Give the player an option to quit at any time
# Reward the player for a correct guess (ex., "Good job!")
# Tell the player how many guesses it took to guess correctly

# As we need to choose a random number, I am importing the random library
import random

# Now I'm going to define a function for my number guessing game.
# The attempts function will keep the track of the players attempt.
def numberGuessingGame():
    secretNumber = random.randint(1, 100)
    attempts = 0

    # Here I am going to print greetings, and some rules for the player.
    print(f"Welcome to the Number Guessing Game!")
    print()
    print(f"Rules: It's a simple game, just 2 things for you:")
    print(f"1. Choose a number from 1 to 100,")
    print(f"2. You can quit any time by typing 'Q'.")
    print()

    # Using while as an infinite loop, will continue until the player wants.
    # using try-except block for handling the exception that may occur.
    while True:
            try:
                playerInput = input("Guess the number: ")
                # This code is for quit the game anytime, when the player wants.
                # If the player input 'q' it will break the loop, and end the game.
                if playerInput.lower() == "q":
                  print(f"Thanks for playing. The correct number was {secretNumber}.")
                  break
                # If the player didn't quit, the code will convert the input into an integer.
                playerGuess = int(playerInput)

                # When player choose any number out of the range, will get this massage.
                # With 'continue' the player is prompted to make another guess.
                if playerGuess < 1 or playerGuess > 100:
                  print("Please enter a number within the range of 1 to 100.")
                  continue
                # It incremented by 1 with each guess.
                attempts += 1
                # This code is for checking whether the player's guess is low or high
                # As the player guess the correct number it will break the code by 'break"
                if playerGuess < secretNumber:
                   print("Wrong guess! Try a higher number.")
                elif playerGuess > secretNumber:
                   print("Wrong guess! Try a lower number.")
                else:
                   print(f"Great! You guessed the correct number {secretNumber} in {attempts} attempts.")
                   break
                # Checking the difference to give a clue for  the player.
                difference = (playerGuess - secretNumber)
                clue = abs(difference)
                if clue <= 5:
                    print("Clue: You're getting closer!")
            # This is for exception.
            except ValueError:
                print("Please enter a valid number.")

# This code allow the script to run directly
# IT ensures that the game is executed only when this script is run directly.
if __name__ == "__main__":
    numberGuessingGame()
