from ContactInfo import ContactInfo
import re
"""
Parse a business card for name, phone number and email

"""
class BusinessCardParser(object):

    def __init__(self):
        self.email_regex = re.compile(r'[^@]+@[^@]+\.[^@]+')
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

        # iterate through each line, checking for one of three matches
        for line in document.split("\n"):

            tmp_name, tmp_confidence = self._getName(line)
            if tmp_confidence > name_confidence:
                name_confidence = tmp_confidence
                name = tmp_name


            # if a previous line found a match, email and number will be defined
            if email is None:
                email = self._getEmail(line)

            if number is None:
                number = self._getNumber(line)

        return ContactInfo(name,number,email)

    
    
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
    
