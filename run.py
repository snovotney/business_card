#!/usr/bin/python

from BusinessCardParser import BusinessCardParser, ContactInfo
from sys import argv

if len(argv) == 1:
    print "%s bc1.txt bc2.txt ..." % (argv[0])
    exit
    
# Initialize parser
parser = BusinessCardParser()
files = []

    
# loop through business cards
for fn in argv[1:]:
    try:
        with open(fn) as f:
            text = f.read()
            info = parser.getContactInfo(text)
    except IOError as e:
        print "I/O Error: ", e
    

    
