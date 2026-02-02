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
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win condition
        word_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False
                break

        if word_guessed:
            print("You saved the snowman!")
            break

        # Check lose condition
        if mistakes >= max_mistakes:
            print("The snowman melted!")
            print("The secret word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter. Try again."
            continue 

        if guess in secret_word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)

        else:
            mistakes += 1
