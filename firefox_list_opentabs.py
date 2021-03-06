#!/usr/bin/env python
import json
import sys
import os

# edit FIREFOX_DIR to point to your profile
# this is where sessionstore.js is located

FIREFOX_DIR = '/path/to/firefox/profile/' # note trailing "/"

try:
    with open(os.path.join(FIREFOX_DIR, 'sessionstore.js')) as json_data:
        data = json.load(json_data)
except IOError:
    print 'No sessionstore.js file found!'
    sys.exit()

def get_tabs(data):
    for window in data['windows']:
        for tab in window['tabs']:
            i = tab['index'] - 1
            print 'Title => ', tab['entries'][i]['title']
        print '---------------------'


get_tabs(data)
