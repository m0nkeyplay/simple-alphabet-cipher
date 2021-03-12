#!/usr/bin/env python3

#   author:		https://github.com/m0nkeyplay
#   August 25, 2020 - original script written
#   Updated Aug 30 to add punctuation
#   Updated Sept 2 to make it simpler.  Simple is good.
#   Updated March 3, 2021 - not everthing needs to be lower case
#                         - may as well add digits too
#                         - Keep your mask on

#   Alphabet cipher module

#   This is a module.  It needs to be called in a script.
#   Call with cac.scramble()
#   This only scrambles letters.
#   I lied.  It does punctuation now too.
#   Not to be used in a production environment to keep secrets
#   Put together based on a dinner conversation
#   and the 7 year old saying "Hey!  What letter is the opposite of A?"

import string

#   dictionary holding the cipher keys and values
cac_ce = {}

#   arrays to get it started
cac_forward = []
cap_forward = []
cad_forward = []

#   fill the arrays
for letter in string.ascii_letters:
    cac_forward.append(letter)

for p in string.punctuation:
    cap_forward.append(p)

#   copy and make the backward array
cac_backward = cac_forward.copy()
cac_backward.reverse()

cap_backward = cap_forward.copy()
cap_backward.reverse()

ca_bdackward = cad_forward.copy()
cad_backward.reverse()

#   make a dictionary that is the cipher
def make_cipher(firstArray,dict,secondArray):
    x = 0
    for var in firstArray:
        dict[var] = secondArray[x]
        x +=1

#   Fill in the cipher dictionaries
make_cipher(cac_forward,cac_ce,cac_backward)
make_cipher(cap_forward,cac_ce,cap_backward)
make_cipher(cad_forward,cac_ce,cad_backward)

#   scramble the text
def scramble(theText):
    stripMe = theText.strip()
    returnMe = ''
    for char in stripMe:
        if char in cac_ce.keys():
            echar = cac_ce[char]
            returnMe += str(echar)
        else:
            returnMe += str(char)
    return returnMe

if __name__ == "__main__":
    print("This should be imported:  import cac")
    exit()
