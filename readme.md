# Window Activity Tracker

This Python script tracks the active application and time spent on each application, with a focus on Google Chrome. It also records the URL of the active tab in Google Chrome.

## Prerequisites

- Python 2.x or 3.x
- macOS environment
- Required Python packages: `AppKit`, `Foundation`

## Installation

No specific installation steps are required. Just ensure that you have the required Python packages installed.

## Usage

1. Run the script in your terminal
2. The script continuously monitors the active window and updates the time spent on each application.
3. If the active window is Google Chrome, it also fetches and logs the URL of the active tab.

## Configuration

- Adjust the time interval in the `time.sleep()` function to control how often the script checks for changes (default is every 5 seconds).
- The script saves the tracked data in a file named `window_data.json`.

## Data Format

The recorded data is stored in JSON format in the `window_data.json` file. Each entry includes the application name, time spent, date, and, for Google Chrome, the URL of the active tab.

Example entry:

```json
{
  "Google Chrome": {
    "Time Spent": 30,
    "Date": "2024-02-29 12:34:56",
    "URL": "https://example.com"
  },
  "Other Application": {
    "Time Spent": 20,
    "Date": "2024-02-29 12:30:00"
  }
}
