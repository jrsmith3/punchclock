#!/usr/bin/python
# In this file I need to do the following:
# 1. Open the punch-in file and create a datetime object from that
# info.
# 2. Grab the current datetime.
# 3. Create an icalendar with a single event the duration of the time 
# between punch-in and punch-out.

import vobject

cal = vobject.iCalendar()
cal.add('vevent')
cal.vevent.add('dtstart').value = \
	datetime.datetime(2006, 2, 16, 9, tzinfo = utc)
cal.vevent.add('dtend').value = \
	datetime.datetime(2006, 2, 16, 18, tzinfo = utc)

print cal.serialize()