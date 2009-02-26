#!/usr/bin/python
"""Record datetime when user logs into KDE

This program is part of the punchclock suite. It simply records the date and 
time of a user's login to KDE and records that information in a simple text 
file. The program punch-out.py does everything else.
"""

__author__ = "Joshua Ryan Smith (joshua.r.smith@gmail.com)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Joshua Ryan Smith"
__license__ = "GPL v3"

import datetime
from dateutil.tz import *

timein = datetime.datetime.now(tzlocal()) + "\n"

# Write current datetime to a temporary file using pickle.
punchin = open('/home/jrsmith3/.kde/share/apps/punchclock/punchin.dat','w')
punchin.write(timein)
punchin.close()
