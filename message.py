#!/usr/bin/env python3

#   author:		https://github.com/m0nkeyplay
#   August 25, 2020 - original script written

#   Simply scramble and descramble cac messages.
#   Take standard input or a file.
#   Returns to screen.  Pipe it if you'd like the data written to a file.

import os
import cac
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text", required=False, help="Scramble/Descramble a message.  Encase message in quotes. Single: Mac/Linux, Double: Windows")
ap.add_argument("-f", "--file", required=False, help="A text file with some text to scramble/descramble")


args = vars(ap.parse_args())

if __name__ == "__main__":
    if args['text']:
        print(cac.scramble(args['text']))    
    if args['file']:
        if not os.path.isfile(args['file']):
            print('\n\nWe can\'t find/open %s.  Please check that it\'s a valid file.\n\n'%args['file'])
            exit()
        else:
            readFile = open(args['file'],'r')
            print(cac.scramble(readFile.read()))
            readFile.close()
    else:
        print("Try -h")