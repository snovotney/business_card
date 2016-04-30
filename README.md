How to run
============

./train_classifier.py -f data/name.model data/train/names.txt 
./parse.py -m data/name.model data/tests/*



Email Extraction
================
isn't rfc-5322 compliant
permissive email

Phone Number Extraction
=======================
- deals with extensions
- american # only
- returns top most phone

Name Extraction
===============
- naive bayes classifier based on 4-grams
- could use a discriminative classifier
- could switch to a sequence model like a NN
- move code to scipy/numpy
- got training data