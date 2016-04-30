import pickle
import random

class TextClassifier(object):
    """ A probabilistic classifier to determine the likelihood 
        that a string of text was generated from a training corpus.

        This model uses a characcter language model to estimate P(w|D)
        where w is the candidate string and D is the corpus of documents
        provided in training.

        We use a first order Markov assumption:

        P(c_1,c_2,...,c_n) = sum log P(c_i | c_{i-1} )
                          
        The first pass uses simple bigram frequencies.

    """

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


    def compute_lklhd(self, string):
        """ Compute the likelihood that a string contains a name

        Args:
            string (str): a string of text, can be mixed-case

        """
        return random.randint(1,5)

    def estimate_model(self, training_files):
        """ Estimate the language model from an array of training samples

        Args:
            training_files (str[]): list of paths to training data
        
        """

        # Read the training data into memory


        # 



        
     
