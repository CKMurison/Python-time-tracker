from stopwatch import Stopwatch
import pygetwindow


def track_time_and_window():

  activeWindow = pygetwindow

  timer = Stopwatch()

  time_tracker = {}

  if activeWindow.isMinimized():
    timer.stop()
    duration = timer.duration
    time_tracker[activeWindow.getActiveWindow] = duration
  
  print(time_tracker)

track_time_and_window()