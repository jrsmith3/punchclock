#!/usr/bin/python
# This script goes into the ~/.kde/Autostart directory. When you log into kde, every script in this directory gets executed.

# Here's how this script should work
# 1. Create an ical event with dtstamp, dtstart, summary = At work, 
# and timezone info.
# 2. Save this half of the event in ~/.kde/share/apps/punchclock with the
# name punch-in.ics
# 3. Add a line to a backup data file. These scripts wind up altering the 
# punchclock.ics file in a way that might cause some corruption. I want to make 
# sure that I don't catastrophically lose data one day by making a backup file.

import datetime
import vobject
from dateutil.tz import *

timenow = datetime.datetime.now(tzlocal())

cal = vobject.iCalendar()
cal.add('vevent')
cal.vevent.add('dtstamp').value = timenow
cal.vevent.add('dtstart').value = timenow
cal.vevent.add('summary').value = "At work"

# Open file to (over)write. 
# !Must fix the hard-coded path.
punchin = open('/home/jrsmith3/.kde/share/apps/punchclock/punchin.ics','w')
punchin.write(cal.serialize())
punchin.close()

# Write some data to a simple text file that can be parsed at a later date:
punchbak = open('/home/jrsmith3/.kde/share/apps/punchclock/punchclock.bak','a')
punchbak.write("in,"+str(datetime.datetime.now())+"\n")
punchbak.close()
