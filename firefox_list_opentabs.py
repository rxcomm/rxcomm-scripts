#!/usr/bin/env python
import json
import sys
import os

# edit FIREFOX_DIR to point to your profile
# this is where sessionstore.js is located

FIREFOX_DIR = '/path/to/your/firefox/profile/directory/' # note trailing "/"

try:
    with open(os.path.join(FIREFOX_DIR, 'sessionstore.js')) as json_data:
        data = json.load(json_data)
except IOError:
    print 'No sessionstore.js file found!'
    sys.exit()

def calendar_open(data):
    for window in data['windows']:
        for tab in window['tabs']:
            for entry in tab['entries']:
                print 'Title => ', entry['title']
        print '---------------------'


calendar_open(data)
