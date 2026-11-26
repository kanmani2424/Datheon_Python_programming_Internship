
import random

# Secret words
words = ["PYTHON", "COMPUTER", "PROGRAM", "HANGMAN", "CODING"]

# Hangman stages
hangman_art = [
    """
     +---+
         |
         |
         |
        ===
    """,
    """
     +---+
     O   |
         |
         |
        ===
    """,
    """
     +---+
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
         |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===
    """,
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===
    """
]


def display_word(secret_word, guessed_letters):
    result = ""

    for letter in secret_word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


def play_game():

    secret_word = random.choice(words)

    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n================================")
    print("       HANGMAN WORD GAME")
    print("================================")

    while wrong_guesses < max_attempts:

        print(hangman_art[wrong_guesses])

        print("Word:", display_word(secret_word, guessed_letters))
        print("Attempts left:", max_attempts - wrong_guesses)

        guess = input("Guess a letter: ").upper().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.")
            continue

        # Duplicate guess checking
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.add(guess)

        # Correct or incorrect guess
        if guess in secret_word:
            print("Correct Guess!")
        else:
            print("Wrong Guess!")
            wrong_guesses += 1

        # Check victory
        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            print("Secret Word:", secret_word)
            return

    # Defeat
    print(hangman_art[max_attempts])
    print("\nGame Over! You lost.")
    print("The secret word was:", secret_word)


play_game()
