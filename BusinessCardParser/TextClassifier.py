import pickle
import random
import re
from collections import defaultdict

class TextClassifier(object):
    """ A probabilistic classifier to determine the likelihood 
        that a string of text was generated from a training corpus.

        This model uses a simple Naive Bayes classifier built on character trigrams

    """

    # These will be filtered out by normalization, so no risk of
    # appearing in normal text -- would extend to <s> or </s> if using arrays
    START_TOKEN = '^'
    STOP_TOKEN  = '#'
    UNK_TOKEN   = '$'
    
    NGRAM_LENGTH = 4  # extract trigrams
    LAMBDA = 0.01     # add-lambda smoothing
    
    def __init__(self,model_file=None):
        """ Load model from disk

        Args:
            model_file (str): path to pickled model object

        """
        self.model = None

        if model_file:
            self.read_model(model_file)
            

    def read_model(self,model_file):
        """ Read in a model file from disk

        Args:
            model_file (str): path to a model file

        """
        
        try:
            f = open(model_file,'rb')
            self.model = pickle.load(f)
        except IOError as e:
            print "I/O Error: ", e
        print "Read model from ", model_file


    def write_model(self, model_file):
        """ Write model file to disk as a txt file

            Will overwrite model if it exists

        Args:
            model_file (str): path to write

        """
        try:
            f = open(model_file,'wb')
            pickle.dump(self.model, f)
        except IOError as e:
            print "I/O Error: ", e
        print "Wrote model to ", model_file


    def score(self, string):
        """ Compute the likelihood that a string contains a name

        Args:
            string (str): a string of text, can be mixed-case

        Returns:
            score: the per-character normalized score of the string
        """

        # normalize and map to feature vector
        vector = self._featurize(string)

        # accumulate log probability
        score = 0
        if len(string) == 0:
            return score

        for feature in vector:

            # map to UNK token if unseen in training data
            if feature not in self.model:
                feature = self.UNK_TOKEN

            s = self.model[feature]
            score += s

        score /= len(vector)
        print score, string
        
        return score

    def estimate_model(self, training_files):
        """ Estimate the language model from an array of training samples

        Args:
            training_files (str[]): list of paths to training data
        
        """
        data = []
        # Read the training data into memory
        for fn in training_files:
            try:
                with open(fn) as f:
                    data.extend(list(f.read().split("\n")))
            except IOError as e:
                print "I/O Error: ", e

        # Convert samples to sparse vectors and normalize input
        data =  map (self._featurize, data)

        # accumulate counts over the entire data set
        counts = defaultdict(int)
        total = 0
        for sample in data:
            for k, v  in sample.iteritems():
                counts[k] += v
                total += v

        # unique number of elements in the dict
        # + one for the UNK token
        V = len(counts) + 1


        # add 10% probability mass for all unseen trigrams
        # could improve by estimating OOV rate or backing off to unigrams
        counts[self.UNK_TOKEN] = 0.00001 * total
        total *= 1.00001
        # Now set the probabilities from the model
        # using add-lambda smoothing

        # P(x)  = c(x) + lambda
        #         -------------
        #         N + V * lambda
        #
        # where N is sum_x c(x)
        #       V = unique number of x

        self.model = {}

        for tgr, c in counts.iteritems():
            self.model[tgr] = (c + self.LAMBDA ) / ( total + V * self.LAMBDA)
            
        # sanity check to make sure prob estimation isn't messed up
        tot = 0
        for tgr ,p in self.model.iteritems():
            tot += p

        if (tot - 1.0 > 0.0000000001):
            raise Exception("Probabilities do not sum to 1, something went wrong")

        print "Estimated Naive Bayes model using %d-grams. %d elements seen in training" %  (self.NGRAM_LENGTH, len(self.model))
        print "%d examples used in training" % (len(data))
        
    def _featurize(self, string):
        """ return a sparse vector of character trigram

        Args:
            string (str): input string
        Returns:
            vec (dict): sparse vector of character trigrams 
        """
        norm = self._normalize(string)

        # extract all n-grams 
        vec = {}

        for i in  range(self.NGRAM_LENGTH,len(norm)+1):
            tgr = norm[i-self.NGRAM_LENGTH:i]
            if vec.get(tgr):
                vec[tgr] += 1
            else:
                vec[tgr] = 1

        return vec
            
        
    def _normalize(self, string):
        """ normalize a string to internal representation

            - append start/stop token
            - lower case
            - map anything not [a-z. ] to UNK
            - remove duplicate spaces

        Args:
            string (str): unnormalized text

        Returns:
            a normalized string
        """
        lc = re.sub(r'[^0-9a-z\. ]',self.UNK_TOKEN, string.lower())
        return self.START_TOKEN + lc + self.STOP_TOKEN
        
        
