#!/usr/bin/python
import vobject
import datetime

# In this file I need to do the following:
# 1. Open the punch-in file as an ical event object

# 2. add dtend
cal.vevent.add('dtend').value = datetime.datetime.now()

# 3. delete the temporary file punch-in.txt

# 4. add the event to a specified icalendar. If that icalendar doesn't
# exist, create it.

print cal.serialize()