# Author: Dmitriy.S - Dhotspot.dev
# Update: 05/22/26
# Ver   : Release 1.2
# About : This is a combination guess game, where the user guesses a four digit combination. 
# If it's wrong, they get a hint, and until the combination is correct, the user can keep guessing. I did not include running_time for this program, so people don't get confused with the numbers.

"""This is an open source program, meaning that the code is open to the public, 
and may be used by anyone as desired, as well as sold. If there are any issues or ideas,
open a new issue on this repo, and include the information."""

import random as rn
def CombinationGuess():
    random_combo = rn.randrange(0000, 9999)

    while True:
        guess = int(input("Input your combination guess: "))
        if guess > 9999 or guess < 0000: # Error handling
            print("Number is out of range. Guess between 0000 and 9999.")
        if guess == random_combo: # If combo is correct
            print("Correct combination!")
            break
        if abs(guess - random_combo) == 20:
             print("Guess combination is 20 numbers off!")
        else: # If combo is wrong.
            hint = input("Combination is wrong. Would you like a hint? (y/n)")
            if hint == "y":
                print("The first two numbers of the combination are %.2s" % int(random_combo/100))
            else:
                continue

if __name__ == "__main__":
     CombinationGuess()
