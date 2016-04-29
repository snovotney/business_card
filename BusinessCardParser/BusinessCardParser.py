from ContactInfo import ContactInfo
"""
Parse a business card for name, phone number and email

"""
class BusinessCardParser(object):

    def __init__(self):
        """ TODO """
        pass

    def getContactInfo(self,document):
        """ Extract contact information from business card
        
        Args:
            document (str): newline separated text from OCR

        Returns:
            ContactInfo: object containing name, phone, email parsed from the text

        Raises:
            TODO
        """
        info = ContactInfo()
        return info

    
