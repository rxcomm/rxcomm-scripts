#!/usr/bin/env python
import json
import sys
import os

# edit FIREFOX_DIR to point to your profile
# this is where sessionstore.js is located

FIREFOX_DIR = '/path/to/your/firefox/profile/directory/' # note trailing "/"
BROWSER_CMD = '/usr/bin/firefox -url calendar.google.com'

try:
    with open(os.path.join(FIREFOX_DIR, 'sessionstore.js')) as json_data:
        data = json.load(json_data)
except IOError:
    os.system(BROWSER_CMD)
    sys.exit()

def calendar_open(data):
    for window in data['windows']:
        for tab in window['tabs']:
            for entry in tab['entries']:
                if entry['title'] == 'Google Calendar':
                    return True
    return False

if not calendar_open(data):
    os.system(BROWSER_CMD)
