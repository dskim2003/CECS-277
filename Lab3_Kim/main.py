# Name: David Kim
# Date: 09/11/2024
# Desc: Hangman game
import string

from dictionary import words
import random

def display_gallows(num_incorrect):
    """
    Displays gallows progression depending on number of incorrect guesses.
    Args:
        num_incorrect: number of incorrect guesses made by user
    Returns:

    """
    print("========")
    if num_incorrect == 0:
        print("||/  |")
        print("||")
        print("||")
        print("||")
        print("||")
    if num_incorrect == 1:
        print("||/  |")
        print("||   o")
        print("||")
        print("||")
        print("||")
    if num_incorrect == 2:
        print("||/  |")
        print("||   o")
        print("||   |")
        print("||")
        print("||")
    if num_incorrect == 3:
        print("||/  |")
        print("||   o")
        print("||   |")
        print("||  /")
        print("||")
    if num_incorrect == 4:
        print("||/  |")
        print("||   o")
        print("||   |")
        print("||  / \\")
        print("||")
    if num_incorrect == 5:
        print("||/  |")
        print("||  \o")
        print("||   |")
        print("||  / \\")
        print("||")
    if num_incorrect == 6:
        print("||/  |")
        print("||  \o/")
        print("||   |")
        print("||  / \\")
        print("||")
def display_letters(letters):
    """
    Displays a list of letters
    Args:
        letters: list of letter to be displayed
    Returns:

    """
    print(*letters)
def get_letters_remaining(incorrect, correct):
    """
    Removes all used letters
    Args:
        incorrect: list of all incorrect guesses made by the user
        correct: list of all correct guesses made by the user
    Returns:
        list of unused letters
    """
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for x in incorrect:
        if x in alphabet:
            alphabet.remove(x)
    for x in correct:
        if x in alphabet:
            alphabet.remove(x)
    return alphabet

def main():
    while True:
        print("-Hangman-")
        incorrect = int(0)
        correct = int(0)
        incorrect_guesses = []
        correct_guesses = ["_", "_", "_", "_", "_", ]
        # Chooses random word from provided file
        target_word = words[random.randint(0, len(words))]
        while True:
            print("Incorrect selections: ")
            print(*incorrect_guesses)
            display_gallows(incorrect)
            print(*correct_guesses)
            print("Letters remaining: ")
            display_letters(get_letters_remaining(incorrect_guesses, correct_guesses))
            # Takes letter input from user
            # Checks if input is correct or not
            while True:
                user_input = input("Enter a letter: ")
                if user_input not in string.ascii_letters:
                    print("That is not a letter.")
                    continue
                else:
                    break
            if user_input.upper() in target_word:
                print("Correct!")
                temp = 0
                # Adds input to list of correct guesses
                for x in target_word:
                    if x == user_input.upper():
                        correct_guesses[temp] = user_input.upper()
                        correct += 1
                    temp += 1
            else:
                print("Incorrect!")
                # Adds input to list of incorrect guesses
                incorrect_guesses.append(user_input.upper())
                incorrect += 1
            if incorrect == 6:
                display_gallows(6)
                print("Correct Word was " + target_word)
                print("You lose!")
                break
            if correct == 5:
                print("You win!")
                break
        if input("Play again? (Y/N) ").lower() == "n":
            break
        else:
            continue
    return 0
main()