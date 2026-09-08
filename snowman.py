"""Startversion für das Spiel Snowman Meltdown mit ASCII-Anzeige."""

import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII art stages
STAGES = [
    """
     _===_
    (o o)
    ( : )
    ( : )
    """,
    """
     _===_
    (o o)
    ( : )
    _ : _
    """,
    """
     _===_
    (o o)
    _ : _
    """,
    """
     _===_
    _ : _
    """,
]


def get_random_word():
    """Selects and returns one random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman phase and the currently revealed secret word."""
    stage_index = min(mistakes, len(STAGES) - 1)
    print(STAGES[stage_index])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)
    print(f"Mistakes: {mistakes}")


def play_game():
    """Begrüßt den Nutzer und verarbeitet einen ersten geratenen Buchstaben."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    # TODO: Build the full game loop here later.
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)

    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()