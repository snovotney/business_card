#!/usr/bin/python
from BusinessCardParser.TextClassifier import TextClassifier
from optparse import OptionParser
import mimetypes
"""
Train a classifier based on training text provided in arguments and write to file

The input file should contain one example of a name per line, case does not matter

DR. BOB SMITH
BOB E. JOHNSON
BOB
BOB SMITH

While the input may be mixed-case, all data is mapped to lower case internally
for this simple prototype.


The output is a pickled object for use in parse.py.
"""

usage = 'train.py [options] train_text1 train_text2 ...'
opt_parser = OptionParser()
opt_parser.add_option('-f', '--file', dest="model_file",
                  help="write name classifier to FILE")

(options, args) = opt_parser.parse_args()

if len(args) == 0:
    print usage
    opt_parser.print_help()
    exit()

if options.model_file is None:
    print "Must pass in model_file to store output"
    exit(1)

# Train the classifier
classifier = TextClassifier()
classifier.estimate_model(args)
classifier.write_model(options.model_file)
