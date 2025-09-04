import re

def parse_log_line(line):
    pattern = re.compile(
        r'(?P<ip>\S+) - - \[(?P<datetime>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) HTTP/\d.\d" (?P<status>\d{3}) (?P<size>\d+)'
    )
    match = pattern.match(line)
    return match.groupdict() if match else None



