# Author: Dmitriy.S - Dhotspot.dev
# Date  : 07/07/25
# Version: First Rel
# About : This is a simple program, which takes the user's input for how many times to flip a coin.
# With more tosses, the percentage of each side comes closer to 100%. The principle here is, that this coin here is more fair than a physical coin, since there is less human error.
# The running_time is another feature that I found to be interesting for those interested people out there.

"""Please note, this program is in no way making anyone profit, and is open source.
   You may do whatever, however, but I would like to see this being used for studies or in classrooms for learning.
    If you can think of any other features for this program, please open a new issue."""

import random as rn
import time # Used to time the program in the "running_time" function.

def cointoss(coin = ['heads', 'tails']):
    tosses = int(input("How many times would you like to toss? : "))
    # The tosses cannot be less than 0, but also limited to 100, if you'd like, you can change the value.
    while tosses < 1 or tosses > 100:
        tosses = int(input("Oops! You've entered an integer that's out of range. How many times would you like to toss? : "))
    else:
        for i in range(tosses):
            print(rn.choice(coin))

def running_time(): # This function times the programs running time, and stops once the numbers have reached the end.
         start_time = time.time()
         cointoss(coin = ['heads', 'tails'])
         end_time = time.time()
         print("This programs running time in s: %s" % (end_time - start_time))
         

if __name__ == "__main__":
        running_time() # The main code is called inside of the "running_time" function.
