from __future__ import print_function
from AppKit import NSWorkspace
import time
from Foundation import *
import json
from datetime import datetime

window_data = {}
active_window_name = ""

while True:
    current_time = datetime.now()
    url = None
    new_window_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

    if active_window_name != new_window_name:
        if active_window_name in window_data:
            window_data[active_window_name]['Time Spent'] += 10
        else:
            window_data[active_window_name] = {'Time Spent': 10, 'Date': str(current_time)}

        active_window_name = new_window_name
        print(active_window_name)

    if active_window_name == 'Google Chrome':
        text_of_MyScript = 'tell application "Google Chrome" to get URL of active tab of window 1'
        s = NSAppleScript.alloc().initWithSource_(text_of_MyScript)
        results, err = s.executeAndReturnError_(None)
        url = results.stringValue()
        print(f"URL: {url}")

        if 'Google Chrome' in window_data:
            window_data['Google Chrome']['Time Spent'] += 10
            window_data['Google Chrome']['URL'] = url
        else:
            window_data['Google Chrome'] = {'Time Spent': 10, 'Date': str(current_time), 'URL': url}

    time.sleep(5)

    with open('window_data.json', 'w') as json_file:
        json.dump(window_data, json_file, indent=2)
