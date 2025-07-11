# Author: Dmitriy.S - Dhotspot.dev
# Date  : 07/08/25
# Version: First Rel
# About : This M8Ball or "Magic 8 Ball" program is one that I've worked on in the past, but only in Java. This time, it is in Python, and I've also added
# the running_time feature here too. The program will run, ask the user for a question, and return a random answer out of the 15 possible ones. During the process, it will be timed.

"""Please note, this program is in no way making anyone profit, and is open source.
   You may do whatever, however, but I would like to see this being used for studies or in classrooms for learning.
    If you can think of any other features for this program, please open a new issue."""

import random as rn
import time

def game():
   start_time = time.time()
   ans_list = ["Magic 8 Ball: It is certain", 
   "Magic 8 Ball: It is decidedly so.",
   "Magic 8 Ball: Without a doubt.",
   "Magic 8 Ball: Yes, definitely", 
   "Magic 8 Ball: The outlook is good.",
   "Magic 8 Ball: You may rely on it.",
   "Magic 8 Ball: Ask again later.",
   "Magic 8 Ball: Better not tell you now.", 
   "Magic 8 Ball: Cannot predict now.", 
   "Magic 8 Ball: Concentrate and try again.",
   "Magic 8 Ball: Reply hazy, try again.",
   "Magic 8 Ball: Outlook not so good.", 
   "Magic 8 Ball: Very doubtful.", 
   "Magic 8 Ball: My reply is no.",
   "Magic 8 Ball: My sources say no."]

   question = input(("Ask your question:"))
   print(rn.choice(ans_list))
   end_time = time.time()
   running_time = (end_time - start_time)

   print("Program's running time in s: %s" % running_time)

if __name__ == "__main__":
   game()
