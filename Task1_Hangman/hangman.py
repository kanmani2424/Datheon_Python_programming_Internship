import random
from pathlib import Path


# LOAD WORDS FROM TXT FILE


file_path = Path(__file__).parent / "google-10000-english-no-swears.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        words = [
            word.strip().upper()
            for word in file
            if word.strip().isalpha()
        ]

except FileNotFoundError:
    print("Error: Word list file not found!")
    print("Please keep the TXT file in the same folder.")
    exit()

if not words:
    print("Error: No words found in the file!")
    exit()


# HANGMAN ASCII ART


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


# DISPLAY HIDDEN WORD


def display_word(secret_word, guessed_letters):

    result = ""

    for letter in secret_word:

        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


# MAIN GAME


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

        guess = input("\nGuess a letter: ").strip().upper()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter!")
            continue

        # Check repeated guess
        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.add(guess)

        # Check correct or wrong guess
        if guess in secret_word:
            print("Correct Guess!")
        else:
            print("Wrong Guess!")
            wrong_guesses += 1

        # Check winning condition
        if all(letter in guessed_letters for letter in secret_word):

            print("\n================================")
            print("       YOU WON!")
            print("================================")

            print("Secret Word:", secret_word)
            return

    # Game over
    print(hangman_art[max_attempts])

    print("\n================================")
    print("       GAME OVER!")
    print("================================")

    print("You lost!")
    print("Secret Word:", secret_word)


# START GAME


play_game()
