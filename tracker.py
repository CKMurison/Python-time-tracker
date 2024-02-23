from stopwatch import Stopwatch
import pygetwindow as getWindow


def track_time_and_window():

  activeWindow = getWindow

  timer = Stopwatch()

  time_tracker = {}

  while activeWindow.isMaximised():
    timer
    time_tracker[activeWindow.getActiveWindow]

  if activeWindow.isMinimized():
    timer.stop()
    duration = timer.duration
    time_tracker[activeWindow.getActiveWindow] = duration
  
  print(time_tracker)

track_time_and_window()
