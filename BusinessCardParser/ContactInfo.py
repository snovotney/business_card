class ContactInfo(object):
    """ Store the parsed contents of a business card

    - Name
    - Email
    - Phone Number

    """

    def __init__(self, name=None, number=None, email=None):
        """ Initialize a contact

        Args:
        name (optional str): First and last name
        number (optional str): Phone number
        email (optional str): email address

        """
        
        self.name = name
        self.number = number
        self.email = email

    def __str__(self):
        """ String summary of contact """
        return "Name: %s\nPhone: %s\nEmail: %s\n" % (self.name, self.number, self.email)

    def getName(self):
        """str: first and last name"""
        return self.name

    def getPhoneNumber(self):
        """str: digits-only phone number"""
        return self.number

    def getEmailAddress(self):
        """str: email address """
        return self.email

