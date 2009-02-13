#!/usr/bin/python
# In this file I need to do the following:
# 1. Open the punch-in file as an ical event object
# 2. add dtend
# 3. delete the temporary file punch-in.txt
# 4. add the event to a specified icalendar. If that icalendar doesn't
# exist, create it.

import vobject
import datetime

cal = vobject.iCalendar()
cal.add('vevent')
cal.vevent.add('dtstart').value = \
	datetime.datetime(2009, 2, 12, 9)
cal.vevent.add('dtend').value = \
	datetime.datetime(2009, 2, 12, 18)

print cal.serialize()