#!/usr/bin/python

from BusinessCardParser import BusinessCardParser, ContactInfo
from optparse import OptionParser


# Read in options
usage = 'parse.py [options] file1 file2 ...'
opt_parser = OptionParser()
opt_parser.add_option('-m', '--model', dest="model_file",
                  help="read name classifier from MODEL_FILE")

(options, args) = opt_parser.parse_args()

if len(args) == 0:
    print usage
    opt_parser.print_help()
    exit()

# Initialize parser
parser = BusinessCardParser(options.model_file)

# loop through business cards
for fn in args:
    try:
        with open(fn) as f:
            text = f.read()
            print text
            info = parser.getContactInfo(text)

            if info.getName() is None:
                print "Could not extract name from %s" % (fn)
            if info.getPhoneNumber() is None:
                print "Could not extract number from %s" % (fn)
            if info.getEmailAddress() is None:
                print "Could not extract email from %s" % (fn)

            print info
    except IOError as e:
        print "I/O Error: ", e
    

    
