"""Spiellogik für Snowman Meltdown."""

import random

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Wählt ein zufälliges geheimes Wort aus der Wortliste aus."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Zeigt Schneemann-Phase, verdecktes Wort und Fehlversuche an."""
    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    print(display_word)
    print(f"Mistakes: {mistakes}/{MAX_MISTAKES}")


def word_is_guessed(secret_word, guessed_letters):
    """Gibt True zurück, wenn jeder Buchstabe des Wortes geraten wurde."""
    return all(letter in guessed_letters for letter in secret_word)


def get_guess(guessed_letters):
    """Fragt einen neuen einzelnen Buchstaben ab."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        return guess


def play_game():
    """Startet das Spiel und verarbeitet richtige sowie falsche Buchstaben."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1
            print("Wrong guess!")
        else:
            print("Correct guess!")

        if word_is_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("You saved the snowman! You won!")
            return

    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"The snowman melted! The word was: {secret_word}")