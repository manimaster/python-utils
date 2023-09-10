import re
import json

class LogParser:
    def __init__(self):
        self.patterns = {}

    def add_pattern(self, name, pattern):
        """Add a new pattern to the parser."""
        self.patterns[name] = re.compile(pattern)

    def remove_pattern(self, name):
        """Remove a pattern from the parser."""
        if name in self.patterns:
            del self.patterns[name]

    def parse(self, log_line):
        """Parse a log line according to the added patterns."""
        results = {}

        for name, pattern in self.patterns.items():
            match = pattern.search(log_line)
            if match:
                results[name] = match.groupdict()

        return results

    def parse_file(self, file_path):
        """Parse a log file and return matches for each line."""
        results = {}

        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                results[line_num] = self.parse(line)

        return results

    def to_json(self, data):
        """Convert the parsed data to JSON format."""
        return json.dumps(data, indent=4)


parser = LogParser()

# Add patterns with named capture groups
parser.add_pattern("ipPattern", r'(?P<ip>\d+\.\d+\.\d+\.\d+)')
parser.add_pattern("datePattern", r'(?P<date>\d{4}-\d{2}-\d{2})')
parser.add_pattern("timePattern", r'(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})')
parser.add_pattern("levelPattern", r'(?P<level>INFO|ERROR|DEBUG|WARN)')

# Sample log line
log_line = "2023-09-11 12:30:45 INFO 192.168.1.1 Connected successfully"

# Parse the log line
result = parser.parse(log_line)

# Print results
print(parser.to_json(result))

# Parse a log file
file_results = parser.parse_file("path_to_log_file.log")
print(parser.to_json(file_results))
