#!/usr/bin/python
# This script goes into the ~/.kde/Autostart directory. When you log into kde, every script in this directory gets executed.

# Here's how this script should work
# 1. Create an ical event with dtstamp, dtstart, summary = At work, 
# and timezone info.
# 2. Save this half of the event in an appropriate location with the
# name punch-in.txt

import datetime
