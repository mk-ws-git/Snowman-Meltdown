# game_logic.py

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list"""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters, wrong_letters):
    # Displays the snowman stage for the current number of mistakes
    print("=" * 30)    
    print(STAGES[mistakes])
    print("-" * 30)

    # Build a display version of the secret word
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:")
    print(display_word.strip())
    print()
    
    print("Wrong guesses:")
    if wrong_letters:
        print(" ".join(sorted(wrong_letters)))
    else:
        print("(none)")
    print()

    print(f"Mistakes: {mistakes}/{len(STAGES) - 1}")
    print("=" * 30)
    print()

def ask_replay():
    while True:
        answer = input("Play again? (y/n): ").lower().strip()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    wrong_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("=" * 30)
    print("Welcome to Snowman Meltdown!")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters, wrong_letters)

        # Check win condition
        word_guessed = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_guessed = False
                break

        if word_guessed:
            print("You saved the snowman!")
            print("=" * 30)
            print()
            break

        # Check lose condition
        if mistakes >= max_mistakes:
            print("The snowman melted!")
            print("The secret word was:", secret_word)
            print("=" * 30)
            print()
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter. Try again.")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
        
        else:
            wrong_letters.append(guess)
            mistakes += 1

    if ask_replay():         
        play_game()
    else:
        return

	
