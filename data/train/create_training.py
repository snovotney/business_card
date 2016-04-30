import random

""" Construct artificial training data of sample names

    create_training.py > names.txt
"""


first_names = list(set(open('first_names.txt','r').read().split()))
last_names = list(set(open('last_names.txt','r').read().split()))

middle_initials = [x[0] for x in first_names]

# generate 5000 examples
for _ in xrange(10000):

    # uniformly samples, could sample from distribution 
    first = random.choice(first_names)
    last  = random.choice(last_names)

    # assume 10% of people put their middle names
    if random.random() > 0.9:

        # assume 90% of people only put their initial
        if random.random() > 0.1:
            middle = random.choice(middle_initials) + '.'
        else:
            middle = random.choice(first_names)
        print first, middle, last
    else:
        print first, last
