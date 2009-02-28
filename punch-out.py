#!/usr/bin/python
"""Record when a user logs in and out of KDE as an iCalendar file.

This program is part of the punchclock suite. Along with punch-in.py it 
generates and iCalendar file with the users login and logout data as events. 
This program takes the login data that the punch-in.py program generated along
with the current datetime and turns this data into an iCanedar event. The 
program then adds this event to an iCalendar file containing other such events,
or creates the ics file if none exists. This program also records the login and
logout data to a separate text file as a backup.
"""

__author__ = "Joshua Ryan Smith (joshua.r.smith@gmail.com)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Joshua Ryan Smith"
__license__ = "GPL v3"

import vobject
import datetime
import pickle
from dateutil.tz import *

# Here's how the program needs to work out: Read in the login time from the previously written pickled data. Generate the logout data. Try to open the target ics file. If it doesn't exist, create a new iCalendar object. If the file does exist, open it and grab the iCalendar object. Add the new event. Write iCalendar object to file. Record login/logout data to the backup text file.

# Collect the datetime of the login event.
punchin = open('/home/jrsmith3/.kde/share/apps/punchclock/punchin.dat','rb')
timein = pickle.load(punchin)
punchin.close()

# Collect the datetime of logout.
timeout = datetime.datetime.now(tzlocal())

# Try to open the iCalendar file. If it doesn't exist, create it.
try:
	punchfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.ics','r')
	caltxt = punchfile.read()
	punchfile.close()

	# Turn that string into a vobject
	cal = vobject.readOne(caltxt)
except:
	cal = vobject.iCalendar()

# Generate an iCalendar event.
cal.add('vevent')
cal.vevent.add('dtstamp').value = timein
cal.vevent.add('dtstart').value = timein
cal.vevent.add('dtend').value = timeout
cal.vevent.add('summary').value = "At work"

# Write the iCalendar back to a file. Clobber any existing file.
punchfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.ics','w')
punchfile.write(cal.serialize())
punchfile.close()

# Record login/logout events in a separate text file for backup.
punchclockbackupfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclockbackup.txt','a')
punchclockbackupfile.write("in,"+str(timein)+"\n")
punchclockbackupfile.write("out,"+str(timeout)+"\n")
punchclockbackupfile.close()





# ========= vvv Old code from punch-in.py vvv =================================
#cal = vobject.iCalendar()
#cal.add('vevent')
#cal.vevent.add('dtstamp').value = timenow
#cal.vevent.add('dtstart').value = timenow
#cal.vevent.add('summary').value = "At work"

## Open file to (over)write. 
## !Must fix the hard-coded path.
#punchin = open('/home/jrsmith3/.kde/share/apps/punchclock/punchin.ics','w')
#punchin.write(cal.serialize())
#punchin.close()

## Write some data to a simple text file that can be parsed at a later date:
#punchbak = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.bak','a')
#punchbak.write("in,"+str(datetime.datetime.now())+"\n")
#punchbak.close()
# ========= ^^^ Old code from punch-in.py ^^^ =================================








# In this file I need to do the following:
# 1. Open the punch-in file and get the data as a string, then close the file.
# !Must fix the hard-coded path.
punchin = open('/home/jrsmith3/.kde/share/apps/punchclock/punchin.ics','r')
caltxt = punchin.read()
punchin.close()

# Turn that string into a vobject
cal = vobject.readOne(caltxt)

# 2. add dtend
cal.vevent.add('dtend').value = datetime.datetime.now(tzlocal())

# 3. delete the temporary file punchin.ics

# 4. add the event to a specified icalendar. If that icalendar doesn't
# exist, create it.

# Open specified icalendar
try:
	punchfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.ics','r')
	punchtxt = punchfile.read()
	punchfile.close()

	punchclockcal = vobject.readOne(punchtxt)
	punchclockcal.vevent_list.append(cal.vevent_list[0])

	# Clobber the old punchclock icalendar by writing one with the new data.
	punchfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.ics','w')
	punchfile.write(punchclockcal.serialize())
	punchfile.close()
except:
	punchfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.ics','w')
	punchfile.write(cal.serialize())
	punchfile.close()

# Write some data to a simple text file that can be parsed at a later date:
punchbak = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.bak','a')
punchbak.write("out,"+str(datetime.datetime.now())+"\n")
punchbak.close()
