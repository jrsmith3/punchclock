#!/usr/bin/python
# In this file I need to do the following:
# 1. Open the punch-in file and create a datetime object from that
# info.
# 2. Grab the current datetime.
# 3. Create an icalendar with a single event the duration of the time 
# between punch-in and punch-out.

import vobject
import datetime

cal = vobject.iCalendar()
cal.add('vevent')
cal.vevent.add('dtstart').value = \
	datetime.datetime(2009, 2, 12, 9)
cal.vevent.add('dtend').value = \
	datetime.datetime(2009, 2, 12, 18)

print cal.serialize()