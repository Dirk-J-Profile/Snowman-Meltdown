"""Spiellogik für Snowman Meltdown."""

import random
import sys

from ascii_art import STAGES


WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Wählt ein zufälliges geheimes Wort aus der Wortliste aus."""
    return random.choice(WORDS)


def clear_screen():
    """Schiebt alte PyCharm-Ausgaben aus dem sichtbaren Bereich."""
    print("\n" * 50, end="")
    sys.stdout.flush()


def display_game_state(mistakes, secret_word, guessed_letters):
    """Löscht alte Inhalte und zeigt den aktuellen Spielstatus an."""
    clear_screen()

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    guessed = ", ".join(sorted(guessed_letters)) or "-"

    print("\n" + "=" * 42)
    print(STAGES[mistakes].strip("\n"))
    print("-" * 42)
    print(f"{'Wort:':<18}{display_word}")
    print(f"Geratene Buchstaben: {guessed}")
    print(f"{'Fehlversuche:':<18}{mistakes}/{MAX_MISTAKES}")
    print("=" * 42)


def word_is_guessed(secret_word, guessed_letters):
    """Gibt True zurück, wenn jeder Buchstabe des Wortes geraten wurde."""
    return all(letter in guessed_letters for letter in secret_word)


def get_guess(guessed_letters):
    """Fragt einen neuen, einzelnen alphabetischen Buchstaben ab."""
    while True:
        guess = input("Rate einen Buchstaben: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Bitte gib genau einen alphabetischen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print("Diesen Buchstaben hast du bereits geraten.")
            continue

        return guess


def ask_to_play_again():
    """Fragt robust ab, ob eine weitere Partie gestartet werden soll."""
    while True:
        answer = input("Noch einmal spielen? (ja/nein): ").strip().lower()

        if answer in {"j", "ja"}:
            return True

        if answer in {"n", "nein"}:
            return False

        print("Bitte antworte mit ja oder nein.")


def play_round():
    """Spielt eine einzelne Partie und gibt True bei einem Sieg zurück."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    while mistakes < MAX_MISTAKES:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        # Alte Anzeige aus dem sichtbaren PyCharm-Bereich schieben.
        clear_screen()

        if guess not in secret_word:
            mistakes += 1
            print("Leider falsch.")

            if mistakes >= MAX_MISTAKES:
                print(
                    "Der Schneemann ist geschmolzen. "
                    f"Das Wort war: {secret_word}"
                )
                return False
        else:
            print("Richtig geraten!")

        if word_is_guessed(secret_word, guessed_letters):
            print(f"Das Wort war: {secret_word}")
            print("Du hast den Schneemann gerettet – gewonnen!")
            return True

        input("Enter für den nächsten Versuch ...")

    return False


def play_game():
    """Startet Partien, bis die Person nicht erneut spielen möchte."""
    print("Willkommen bei Snowman Meltdown!")

    while True:
        play_round()

        if not ask_to_play_again():
            print("Danke fürs Spielen!")
            break

        print("\nNeue Runde – viel Erfolg!")