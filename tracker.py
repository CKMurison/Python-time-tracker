import time
import pygetwindow


def track_time_and_window(time_tracker):

  start_time = time.time()
  
  activeWindow = pygetwindow.getActiveWindow()

  end_time = time.time()

  elapsed_time = end_time - start_time

  time_tracker = {}

