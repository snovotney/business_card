#!/usr/bin/python

from BusinessCardParser import BusinessCardParser, ContactInfo

b = BusinessCardParser()
print b.getContactInfo("foo")

c = ContactInfo('blah','foo','buzz')
print str(c)
