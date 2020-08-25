#!/usr/bin/env python3

#   author:		https://github.com/m0nkeyplay
#   August 25, 2020 - original script written

#   Alphabet cipher module

#   This is a module.  It needs to be called in a script.
#   Call with cac.scramble() and cac.descramble()
#   This only scrambles letters.
#   Not to be used in a production environment to keep secrets
#   Put together based on a dinner conversation
#   and the 7 year old saying "Hey!  What letter is the opposite of A?"

import string

#   dictionaries holding the cipher keys and values
cac_ce = {}
cac_cd = {}

#   array to get it started
cac_forward = []

#   fill the array
for letter in string.ascii_lowercase:
    cac_forward.append(letter)

#   copy and make the backward array
cac_backward = cac_forward.copy()
cac_backward.reverse()

#   fill the scramble dictionary
cacx = 0
for letter in cac_forward:
    cac_ce[letter] = cac_backward[cacx]
    cacx+=1

#   fill the descramble dictionary
cacy = 0
for letter in cac_backward:
    cac_cd[letter] = cac_forward[cacy]
    cacy+=1

#   scramble the text
def scramble(theText):
    lowerMe = theText.lower()
    returnMe = ''
    for char in lowerMe:
        if char in cac_ce.keys():
            echar = cac_ce[char]
            returnMe += str(echar)
        else:
            returnMe += str(char)
    return returnMe

#   descramble the text
def descramble(theText):
    lowerMe = theText.lower()
    returnMe = ''
    for char in lowerMe:
        if char in cac_cd.keys():
            echar = cac_cd[char]
            returnMe += str(echar)
        else:
            returnMe += str(char)
    return returnMe

if __name__ == "__main__":
    print("This should be imported:  import cac")
    exit()
