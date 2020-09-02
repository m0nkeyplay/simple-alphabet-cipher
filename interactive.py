#!/usr/bin/env python3

#   author:		https://github.com/m0nkeyplay
#   August 25, 2020 - original script written

#   Simply scramble and descramble cac messages.
#   Take input from a user.
#   Returns message to screen.
#   Start a conversation about programming and ciphers

import os
import cac

startMessage = """
╔════╗╔═╗╔═╗
╚══╗ ║╚╗╚╝╔╝
  ╔╝╔╝ ╚╗╔╝
 ╔╝╔╝  ╔╝╚╗
╔╝ ╚═╗╔╝╔╗╚╗
╚════╝╚═╝╚═╝
Alphabet Cipher
Let's play with some words!
"""

if __name__ == "__main__":
    print(startMessage)
    startName = input("Hey.  What's your name? ")
    print("Hi %s.  This is your name scrambled in Alphabet Cipher."%cac.scramble(startName))
    while True:
        toDo = input("What would you like to do?\nScramble a message (s)\nDescramble a message (d)\nExit (e)\n")
        if toDo.lower() == "s":
            scrambleMe = input("Great. What would you like to scramble?\n")
            print("\nHere your scrambled message:\n%s\n"%cac.scramble(scrambleMe))
        elif toDo.lower() == "d":
            descrambleMe = input("Great. What would you like to descramble?\n")
            print("\n\nHere your message descrambled:\n%s\n"%cac.scramble(descrambleMe))
        elif toDo.lower() == "e":
            print("Have a great day!")
            exit()
        else:
            print("Please choose s for scramble, d for descramble or e for exit program.")
