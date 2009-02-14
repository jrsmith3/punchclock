#!/usr/bin/python
import vobject
import datetime

# In this file I need to do the following:
# 1. Open the punch-in file and get the data as a string, then close the file.
# !Must fix the hard-coded path.
punchin = open('/home/jrsmith3/.kde/share/apps/punchclock/punchin.ics','r')
caltxt = punchin.read()
punchin.close()

# Turn that string into a vobject
cal = vobject.readOne(caltxt)

# 2. add dtend
cal.vevent.add('dtend').value = datetime.datetime.now()

# 3. delete the temporary file punchin.ics

# 4. add the event to a specified icalendar. If that icalendar doesn't
# exist, create it.

# Open specified icalendar
try:
	punchfile = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.ics','r')
	punchtxt = punchclockfile.read()
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
