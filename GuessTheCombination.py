# Author: Dmitriy.S - Dhotspot.dev
# Date  : 07/17/25
# Ver   : Release 1
# About : This is a combination guess game, where the user guesses a four digit combination. 
# If it's wrong, they get a hint, and until the combination is correct, the user can keep guessing. I did not include running_time for this program, so people don't get confused with the numbers.

"""This is an open source program, meaning that the code is open to the public, 
and may be used by anyone as desired, as well as sold. If there are any issues or ideas,
open a new issue on this repo, and include the information."""

import random as rn

def guess():
    game = True
    combset = range(1111, 9999)
    random_combo = rn.choice(combset)
    
    while game:
        guess = int(input("Input your combination guess: ")) # The first guess, before the hint.
        if guess > 9999 or guess < 0000: # Error handling
            print("Number is out of range. Guess between 0000 and 9999.")
        if guess == random_combo: # If combo is correct
            print("Correct combination")
            quit()
        else: # If combo is wrong.
            hint = input("Combination is wrong. Would you like a hint? (y/n)")
            if hint == "y":
                print("The first two numbers of the combination is %.2s" % int(random_combo/100))
            if hint == "n":
                guess = int(input("Input your combination guess:")) # Second round. There's only two rounds which keep repeating.
                if guess > 9999 or guess < 0000:
                    print("Number is out of range. Guess between 0000 and 9999.")
        if guess == random_combo:
            print("Correct combination")
            quit()
        else:
            print("Combination is wrong.")
                    

if __name__ == "__main__":
            guess()
