import subprocess
import signal
import sys
import re
from collections import Counter

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.error_count = 0
        self.http_status_count = Counter()
        self.keyword_count = Counter()
        self.error_messages = Counter()

    def start_monitoring(self):
        # Process existing logs
        self.process_existing_logs()

        try:
            # Open the log file with tail command in subprocess
            tail_command = ['tail', '-n', '0', '-F', self.log_file]
            self.tail_process = subprocess.Popen(tail_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

            # Continuously monitor for new log entries
            for line in iter(self.tail_process.stdout.readline, ''):
                log_entry = line.strip()

                # Analyze log entry
                self.analyze_log_entry(log_entry)

        except KeyboardInterrupt:
            # Handle keyboard interrupt (Ctrl+C)
            print("\nMonitoring stopped.")
            self.stop_monitoring()

    def stop_monitoring(self):
        if hasattr(self, 'tail_process') and self.tail_process:
            self.tail_process.terminate()  # Terminate the tail subprocess
            self.tail_process.wait()  # Wait for the subprocess to finish

    def process_existing_logs(self):
        try:
            with open(self.log_file, 'r') as file:
                for line in file:
                    log_entry = line.strip()
                    self.analyze_log_entry(log_entry)
        except FileNotFoundError:
            print("Log file not found.")

    def analyze_log_entry(self, log_entry):
        # Count occurrences of error messages
        if 'ERROR' in log_entry:
            self.error_count += 1
            # Extract and track error messages
            error_message = log_entry.split('ERROR', 1)[-1].strip()
            self.error_messages[error_message] += 1

        # Count occurrences of HTTP status codes
        http_status_codes = re.findall(r'\b\d{3}\b', log_entry)
        for status_code in http_status_codes:
            self.http_status_count[status_code] += 1

        # Count occurrences of specific keywords
        for keyword in self.keywords:
            if keyword in log_entry:
                self.keyword_count[keyword] += 1

        # Print the new log entry
        print(log_entry)

        # Print detailed summary reports
        print(f"Total error count: {self.error_count}")
        print("Top error message:")
        if self.error_messages:
            top_error_message, error_count = self.error_messages.most_common(1)[0]
            print(f"{top_error_message}: {error_count}")
        else:
            print("No error messages")
        print("HTTP status code counts:")
        for code, count in self.http_status_count.items():
            print(f"{code}: {count}")
        print("Keyword counts:")
        for keyword, count in self.keyword_count.items():
            print(f"{keyword}: {count}")

    def get_search_keywords(self):
        # Prompt user to input specific keywords to search for
        keywords_input = input("Enter keywords to search for (comma-separated): ")
        self.keywords = [keyword.strip() for keyword in keywords_input.split(',')]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]

    # Create LogAnalyzer instance
    analyzer = LogAnalyzer(log_file_path)

    # Get search keywords from user
    analyzer.get_search_keywords()

    # Start monitoring the log file
    analyzer.start_monitoring()