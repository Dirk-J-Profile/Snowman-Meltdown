"""Minimale Startversion für das Spiel Snowman Meltdown."""

import random


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects and returns one random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """Begrüßt den Nutzer und verarbeitet einen ersten geratenen Buchstaben."""
    secret_word = get_random_word()

    print("Welcome to Snowman Meltdown!")
    print("Secret word selected:", secret_word)

    # TODO: Build the full game loop here later.
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()