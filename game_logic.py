# game_logic.py

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Dispays the snowmand stage for the current number of mistakes
    print(STAGES[mistakes])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print("\n")

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    max_mistakes = len(STAGES) - 1

    while True:
        # Display current game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # End game if word fully guessed
        word_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False
                break
        if word_guessed:
            print("You saved the snowman!")
            break

        # End game if mistake limit reached
        if mistakes >= max_mistakes:
            print("The snowman melted!")
            break

        # Prompt user for a guess
        guess = input("Guess a letter: ").lower()

        # Handle guesses: update guessed letters
        guessed_letters.append(guess)

        # Increment mistakes if guess is wrong
        if guess not in secret_word:
            mistakes += 1
