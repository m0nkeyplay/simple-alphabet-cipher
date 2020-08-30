#!/usr/bin/env python3

#   author:		https://github.com/m0nkeyplay
#   August 25, 2020 - original script written
#   Updated Aug 30 to add punctuation

#   Alphabet cipher module

#   This is a module.  It needs to be called in a script.
#   Call with cac.scramble() and cac.descramble()
#   This only scrambles letters.
#   I lied.  It does punctuation now too.
#   Not to be used in a production environment to keep secrets
#   Put together based on a dinner conversation
#   and the 7 year old saying "Hey!  What letter is the opposite of A?"

import string

#   dictionaries holding the cipher keys and values
cac_ce = {}
cac_cd = {}

#   arrays to get it started
cac_forward = []
cap_forward = []

#   fill the arrays
for letter in string.ascii_lowercase:
    cac_forward.append(letter)

for p in string.punctuation:
    cap_forward.append(p)

#   copy and make the backward array
cac_backward = cac_forward.copy()
cac_backward.reverse()

cap_backward = cap_forward.copy()
cap_backward.reverse()

#   make a dictionary that is the cipher
def make_cipher(firstArray,dict,secondArray):
    x = 0
    for var in firstArray:
        dict[var] = secondArray[x]
        x +=1

#   Fill in the cipher dictionaries
make_cipher(cac_forward,cac_ce,cac_backward)
make_cipher(cap_forward,cac_ce,cap_backward)
make_cipher(cac_backward,cac_cd,cac_forward)
make_cipher(cap_backward,cac_cd,cap_forward)

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
