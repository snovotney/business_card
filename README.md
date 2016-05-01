This package extractes the name, number and email from the text of
business cards.

The code is implemented for python 2.7 and requires no special dependencies.

parse.py - invokes the package to extract info from sample text filess
train_classifier.py - estimates the person name classifier from training data.
BusinessCardParser/ - python package implements the solution.
data/ - training data for name classifier and test data for business cards.

How to run
==========
To parse txt files containing business card output,

> python parse.py -m data/name.model data/tests/*

To train the name model on different data, 
> python train_classifier.py -f data/name.model data/train/names.txt 

Details
=======

Email Extraction
----------------

A lax regex is used. It is not RFC-5322 compliant since that standard
is extremely flexibile.

I assume the @ sign is unlikely to often appear in business cards, so 

Phone Number Extraction
-----------------------

- Only matches U.S. phone numbers (1-111-111-1111)
- Tries to extract extensions if present
- If multiple phone numbers are present, the top-most number
  that indicates a primary number is chosen.

Extensions could add:
- non-U.S. phone numbers
- slot filling to populate work/cell/home

Name Extraction
---------------
A naive bayes classifier built on character 4-grams is used.

Common first and last names came from http://names.mongabay.com/

A training corpus was then randomly generated from theses word
lists. From here, 4-gram frequencies were estimated with a small
smoothing penalty.

Extensions could add:
- a discriminative classifier based on name vs. company or title
- character sequence models built on RNNs/HMMs
- better training based on full names
- move code to scipy/numpy. For dependency simplicity, I did not use
these libraries.
