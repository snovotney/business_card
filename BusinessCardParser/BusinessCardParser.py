from ContactInfo import ContactInfo
import re
"""
Parse a business card for name, phone number and email

"""
class BusinessCardParser(object):

    email_regex = re.compile('[^@]+@[^@]+\.[^@]+')

    # american phone numbers
    phone_regex = re.compile('1?\s?\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}')

    # positive/negative indicators of a primary phone number
    phone_features = {
        'tel':1,
        'telephone':1,
        'phone':1,
        'office':1,
        'work':1,
        'p':1,     # shorthand for phone
        'number':1,
        'direct':1,
        'fax':-1,
        'cell':-1,
        'home':-1,
        'f':-1,       # shorthand for fax
        'mobile':-1
    }

    def __init__(self):
        pass

    def getContactInfo(self,document):
        """ Extract name, email and phone number from a business card

        If multiple lines match a phone number or email, 
        return the candidate closest to the top
        
        
        Args:
            document (str): newline separated text from OCR

        Returns:
            ContactInfo: object containing name, phone, email parsed from the text
        """

        name_confidence = 0
        name = None
        number = None
        email = None
        potential_numbers = []
        
        # iterate through each line, checking for one of three matches
        for line in document.split("\n"):

            tmp_name, tmp_confidence = self._getName(line)
            if tmp_confidence > name_confidence:
                name_confidence = tmp_confidence
                name = tmp_name


            # if a previous line found a match, email and number will be defined
            if email is None:
                email = self._getEmail(line)

            #store all found numbers and the line as context
            number = self._getNumber(line)
            if number is not None:
                potential_numbers.append((number,line))

        # pick the best found number based on the whole line as context
        best_score = -1
        for num, line in potential_numbers:
            score = self._score_line_with_number(line)
            if score > best_score:
                number = num
                best_score = score

        return ContactInfo(name,number,email)

    
    def _score_line_with_number(self,line):
        """ Score a line as likely being a work number"

        Args:
            line (str): A line containing a matched number

        Returns:
            score (float): positive if line is likely a work line, negative if not.

        """
        score = 0
        for word in [word.rstrip(':.') for word in line.lower().split()]:
            if self.phone_features.get(word):
                score += self.phone_features[word]
        return score
                                           
    def _getEmail(self,line):
        """ Parse email from a line of text

        A very permissive regex is used to match against likely emails.
        A full RFC-5322 compliant regex is beyond the scope of this code base.

        Args:
            line (str): a line from a business card

        Returns:
            email (str): extracted email string, None if no match found
        """

        m = re.search(self.email_regex,line)
        if m is not None:
            return m.group(0)
        else:
            return None

    def _getNumber(self,line):
        """ Parse number from a line of text

        Args:
            line (str): a line from a business card

        Returns:
            number (str): extracted number string, None if no match found
        """
        m = re.search(self.phone_regex,line)
        if m is not None:
            return m.group(0)
        else:
            return None


    def _getName(self,line):
        """ Parse first and last name from a line of text

        Args:
            line (str): a line from a business card

        Returns:
            confidence (float): Confidence that the line is a name
            name (str): first and last name
        """        
        return 0, None
    
