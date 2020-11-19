#!/usr/bin/python3

from dateutil.parser import parse
from datetime import datetime

#def is_date(string, fuzzy=False):
#    """
#    Return whether the string can be interpreted as a date.
#
#    :param string: str, string to check for date
#    :param fuzzy: bool, ignore unknown tokens in string if True
#    """
#    try: 
#        parse(string, fuzzy=fuzzy)
#        return datetime.datetime(string)
#
#    except ValueError:
#        return False

#print(is_date("june 20th 2015"))
#print(is_date("wednesday, june 5, 9 a.m."))
#print(is_date("Wednesday, June 5, 9 a.m. Beverly Bank &amp; Trust, 10258 S. Western Ave"))


#d=datetime.now()
#print(d)

#date_string="Wednesday, June 5, 9 a.m. "
#date_string="Wednesday, June 5"
date_string="20 June 2012 09:00"

#print("date_string =", date_string)
#print("type of date_string =", type(date_string))

date_object = datetime.strptime(date_string, "%d %B %Y %H:%M")

print("date_object =", date_object)
print("type of date_object =", type(date_object))
