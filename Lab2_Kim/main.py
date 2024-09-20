# Name: David Kim
# Date: 9/6/2024
# Desc: Rock Paper Scissors against computer

import check_input
import random
from check_input import get_int_range

def weapon_menu():
    while True:
        # Prompts user and takes input
        print("Choose your weapon: \n")
        print("R. Rock\n")
        print("P. Paper\n")
        print("S. Scissors\n")
        print("B. Back\n")
        user_input = input("")

        # Checks for valid input from user
        if user_input == "R":
            return "R"
        if user_input == "P":
            return "P"
        if user_input == "S":
            return "S"
        if user_input == "B":
            return "B"
        else:
            print("Invalid input. Please try again.\n")
            continue

def comp_weapon():
    # Generates random integer and returns R, P, or S
    temp = random.randint(1,3)
    if temp == 1:
        return "R"
    if temp == 2:
        return "P"
    else:
        return "S"

def find_winner(player, comp):
    # Compares user and computer input and determines outcome
    if player == "R":
        if comp == "R":
            print("You played Rock.\n")
            print("Computer played Rock.\n")
            print("Tie.\n")
            return 0
        if comp == "P":
            print("You played Rock.\n")
            print("Computer played Paper.\n")
            print("You lose.\n")
            return 2
        else:
            print("You played Rock.\n")
            print("Computer played Scissors.\n")
            print("You win.\n")
            return 1
    if player == "S":
        if comp == "R":
            print("You played Scissors.\n")
            print("Computer played Rock.\n")
            print("Computer wins.\n")
            return 2
        if comp == "P":
            print("You played Scissors.\n")
            print("Computer played Paper.\n")
            print("You win.\n")
            return 1
        else:
            print("You played Scissors.\n")
            print("Computer played Scissors.\n")
            print("Tie.\n")
            return 0
    else:
        if comp == "R":
            print("You played Paper.\n")
            print("Computer played Rock.\n")
            print("You win.\n")
            return 1
        if comp == "P":
            print("You played Paper.\n")
            print("Computer played Paper.\n")
            print("Tie.\n")
            return 0
        else:
            print("You played Paper.\n")
            print("Computer played Scissors.\n")
            print("You lose.\n")
            return 2

def display_scores(player, comp):
    # Displays current scores
    print("Player = " + str(player) + "\n")
    print("Computer = " + str(comp) + "\n")

def main():
    player_wins = int(0)
    computer_wins = int(0)
    # Loops menu until user inputs exit code
    while True:
        print("RPS Menu\n")
        print("1. Play Game\n")
        print("2. Show Score\n")
        print("3. Quit\n")
        menu_input = get_int_range('',1,3)
        if menu_input == 1:
            while True:
                player_weapon = weapon_menu()
                if player_weapon == "B":
                    break
                output = int(find_winner(player_weapon, comp_weapon()))
                if output == 1:
                    player_wins += 1
                    continue
                if output == 2:
                    computer_wins += 1
                    continue
            continue
        if menu_input == 2:
                display_scores(player_wins, computer_wins)
                continue
        else:
            break
    # Displays final score at end of program
    print("Final Score:\n")
    print("Player = " + str(player_wins) + "\n")
    print("Computer = " + str(computer_wins) + "\n")
    return 0
main()