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
ap.add_argument("-s", "--scramble", required=False, help="Scramble a message.  Encase message in quotes or add -f to scramble a file.")
ap.add_argument("-d", "--descramble", required=False, help="Descramble a message.  Encase message in quotes or add -f to descramble a file.")
ap.add_argument("-sf", "--sfile", required=False, help="A text file with some text to scramble")
ap.add_argument("-df", "--dfile", required=False, help="A text file with some text to descramble")

args = vars(ap.parse_args())

if __name__ == "__main__":
    if args['scramble']:
        print(cac.scramble(args['scramble']))    
    if args['descramble']:
        print(cac.descramble(args['descramble']))
    if args['sfile']:
        if not os.path.isfile(args['sfile']):
            print('\n\nWe can\'t find/open %s.  Please check that it\'s a valid file.\n\n'%args['sfile'])
            exit()
        else:
            readFile = open(args['sfile'],'r')
            print(cac.scramble(readFile.read()))
            readFile.close()
    if args['dfile']:
        if not os.path.isfile(args['dfile']):
            print('\n\nWe can\'t find/open %s.  Please check that it\'s a valid file.\n\n'%args['dfile'])
            exit()
        else:
            readFile = open(args['dfile'],'r')
            print(cac.descramble(readFile.read()))
            readFile.close()