from __future__ import print_function
from AppKit import NSWorkspace
import time
from Foundation import *

active_window_name = ""

while True:
    new_window_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    
    if active_window_name != new_window_name:
        active_window_name = new_window_name
        print(active_window_name)
    
    if active_window_name == 'Google Chrome':
        text_of_MyScript = 'tell application "Google Chrome" to get URL of active tab of window 1'
        s = NSAppleScript.alloc().initWithSource_(text_of_MyScript)
        results, err = s.executeAndReturnError_(None)
        print(results.stringValue())
    
    time.sleep(10)

      