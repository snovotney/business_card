#!/usr/bin/python
from BusinessCardParser import BusinessCardParser, ContactInfo
from optparse import OptionParser

""" Extract name, number and email from text of business cards """

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

if options.model_file is None:
    print "Must pass in model file"
    opt_parser.print_help()
    exit()
    
parser = BusinessCardParser(options.model_file)

print 
# loop through business cards
for fn in args:
    try:
        with open(fn) as f:

            # extract object conforming to the ContactInfo interface
            text = f.read()
            info = parser.getContactInfo(text)

            print "Business card", fn
            print '-' * 40
            print text
            print '-' * 40
            
            if info.getName() is None:
                print "Could not extract name from %s" % (fn)
            if info.getPhoneNumber() is None:
                print "Could not extract number from %s" % (fn)
            if info.getEmailAddress() is None:
                print "Could not extract email from %s" % (fn)

            print info
            print '-' * 40            
    except IOError as e:
        print "I/O Error: ", e
    

    
