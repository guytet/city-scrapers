#!/usr/bin/python3

from dateutil.parser import parse
from datetime import datetime
import re

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

#d=datetime.now()
#print(d)

#date_string="SSA 20: Wednesday June 5 9am"
#date_string="Wednesday, June 5"
#date_string="20 June 2012 09:00"
#date_string="SSA 20: Wednesday, June 5, 9 a.m."

#print("date_string =", date_string)
#print("type of date_string =", type(date_string))
#date_object = datetime.strptime(date_string, "%d %B %Y %H:%M")
#date_object = datetime.strptime(date_string, "%A %B %d %I%p")

#print("date_object =", date_object)
#print("type of date_object =", type(date_object))

#print(re.split((":"), date_string))

li=['2019 SSA Meetings',
'SSA 20: Wednesday, June 5, 9 a.m. Beverly Bank &amp; Trust, 10258 S. Western Ave.',
'Wednesday, July 10, 9 a.m. Beverly Bank &amp; Trust, 10258 S. Western Ave.'
]

# option for joining the three list comprehensions bellow to one line,
# this of course makes for quite a complicated line
#li = [item.split("Bev", 1)[0].split(": ", 1)[-1] for item in li if "Meetings" not in item]                

# look into generator comprehenstion
# last two actions look into 'extract`'
#  - looked into 'extract' - could not find a python
#    method named 'extract'
li = [ item for item in li if "Meetings" not in item ]
li = [ item.split('Bev', 1)[0] for item in li ]
li = [ item.split(': ', 1)[-1] for item in li ]

print(li)

#for item in li:
#  base = [ re.sub(r"\s+", " ", item).lower() for item in base ]

#  item = (item.split(': ', 1)[-1])
#  print(item)
























#  print(re.split( (":"), item))




















































