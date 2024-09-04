#Name: David Kim
#Date: 8/29/2024
#Desc: prompt user to guess number between 1-100


import random
import check_input

def main():
    targetNum = random.randint(1, 100)          # Generates random number between 1-100
    guesses = int(0)

    print('I\'m thinking of a number')

    while True:
        guess = check_input.get_int_range('Make a guess: ', 1, 100)         # Checks to see if user input is valid
        guesses += 1
        if guess > targetNum:
            print('Too High! Guess again.')
            continue
        if guess < targetNum:
            print('Too Low! Guess again.')
            continue
        else:
            print('You got it! It took you ' + str(guesses) + ' tries.')
            break
main()




