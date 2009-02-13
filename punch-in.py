#!/usr/bin/python
# This script goes into the ~/.kde/Autostart directory. When you log into kde, every script in this directory gets executed.

# Here's how this script should work
# 1. Create an ical event with dtstamp, dtstart, summary = At work, 
# and timezone info.
# 2. Save this half of the event in ~/.kde/share/apps/punchclock with the
# name punch-in.ics

import datetime
import vobject

cal = vobject.iCalendar()
cal.add('vevent')
# NEED TIMEZONE INFO!!
cal.vevent.add('dtstamp').value = datetime.datetime.now()
cal.vevent.add('dtstart').value = datetime.datetime.now()
cal.vevent.add('summary').value = "At work"

# This is the part where I save what I have as an icalendar or an ical event.
# Instead, I'm printing it.
print cal.serialize()
