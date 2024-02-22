use this library here --> pygetwindow to obtain the information of the currently active window. For example:
import pygetwindow

print(pygetwindow.getActiveWindow())
_____________________________________________
<Win32Window left="1912", top="-392", width="1096", height="1888", title="tester.py - tester - Visual Studio Code">
Now, you need a way of measuring time. To do this, you can use the builtin time:
import time

start_time = time.time()

end_time = time.time()

elapsed_time = end_time - start_time

print(elapsed_time)

You need to:
Create a dictionary which will hold key value pairs. Key for any given active window, and value for the amount of time this window is active.

Create a function that checks which window is active, and stars measuring time. You then have to periodically check if the window is still open by running pygetwindow.getActiveWindow().

If you detect that pygetwindow.getActiveWindow() is returning a different active window from the previous, stop the time, and update the dictionary value for that window.

Immediatelly start another timer for the newly active window.

Edit:
Please note, that all of this will be stored in memory. So, if your program crashes after you have been using it for a while, all of your data for how long a window was active, will be gone. The next step would be to implement functionality that periodically saves this data to a file, in the event that something goes wrong.


I need to measure my elapsed time against the window that's open and add that to time_tracker{}



while activeWindow.getActiveWinow == true
  timer = stopwatch()
  if activeWindow.isMinimized():
    timer.stop()
    duration = timer.duration
    time_tracker[activeWindow.getActiveWindow] = duration
  
  print(time_tracker)