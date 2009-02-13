#!/usr/bin/python

import re

# open the logfile and dump every line to an element in a list:
logfile = open("auth.log.3","r")
loglines = logfile.readlines()

# Initialize the stack for the logfile lines
logstack = []

# Find lines that look like I logged in via KDM at the keyboard. There's 
# probably a better way to do this, but my guess is that it involves something
# way more sophisticated than I care to learn.
for curline in loglines:
  if re.search(r"\bjrsmith3\b",curline) and re.search(r"\bkdm:\b",curline):
    # append curline to the stack:
    logstack.append(curline)
    
# Now I need to grab the date and other information from the items in logstack
# to have enough information to create login/logout events. I can actually use
# split() to break everything up, then I can reassemble the relevant pieces.
# Its a hack, but it will probably work.
