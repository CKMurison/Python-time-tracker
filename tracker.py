# Importing necessary modules
from __future__ import print_function
from AppKit import NSWorkspace
import time
from Foundation import *
import json
from datetime import datetime

# Dictionary to store window activity data
window_data = {}

# Variable to store the name of the currently active window
active_window_name = ""

# Infinite loop to continuously track window activity
while True:
    # Get the current timestamp
    current_time = datetime.now()
    
    # Variable to store the URL (initialized to None)
    url = None
    
    # Get the name of the currently active application
    new_window_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

    # Check if there's a change in the active window
    if active_window_name != new_window_name:
        # Update time spent for the previous window
        if active_window_name in window_data:
            window_data[active_window_name]['Time Spent'] += 10
        else:
            # Create a new entry for the previous window if it doesn't exist
            window_data[active_window_name] = {'Time Spent': 10, 'Date': str(current_time)}

        # Update the active window name
        active_window_name = new_window_name
        print(active_window_name)

    # Check if the active window is Google Chrome
    if active_window_name == 'Google Chrome':
        # AppleScript to get the URL of the active tab in Google Chrome
        text_of_MyScript = 'tell application "Google Chrome" to get URL of active tab of window 1'
        s = NSAppleScript.alloc().initWithSource_(text_of_MyScript)
        results, err = s.executeAndReturnError_(None)
        
        # Get the URL from the AppleScript results
        url = results.stringValue()
        print(f"URL: {url}")

        # Update time spent and URL for Google Chrome entry in window_data
        if 'Google Chrome' in window_data:
            window_data['Google Chrome']['Time Spent'] += 10
            window_data['Google Chrome']['URL'] = url
        else:
            # Create a new entry for Google Chrome if it doesn't exist
            window_data['Google Chrome'] = {'Time Spent': 10, 'Date': str(current_time), 'URL': url}

    # Pause execution for 5 seconds before checking again
    time.sleep(5)

    # Write the window_data dictionary to a JSON file
    with open('window_data.json', 'w') as json_file:
        json.dump(window_data, json_file, indent=2)

