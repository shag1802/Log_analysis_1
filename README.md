# Log Analyzer README
This repository contains two Python scripts: getlogs.py and log-monitoring.py. These scripts are designed to help with generating and monitoring log files, respectively.

## Prerequisites
Python 3.x installed on your system

## getlogs.py
This script generates dummy log messages with different log levels (INFO, DEBUG, ERROR) at random intervals.

## Usage
Clone or download this repository.
Run the script using the following command:

### Copy code
python3 getlogs.py
The script will continuously generate log messages in the test.log file .

## log-monitoring.py
This script monitors a specified log file for new entries, performs basic analysis on log entries, and generates summary reports.

## Usage
Clone or download this repository.
Navigate to the directory containing log-monitoring.py in your terminal.
Run the script with the path to the log file you want to monitor, for example:

### Copy code
python3 log-monitoring.py /path/to/your/log/file.log

Follow the prompts to enter specific keywords to search for. Separate multiple keywords with commas.
The script will continuously monitor the log file and display detailed summary reports in the console in real-time.
