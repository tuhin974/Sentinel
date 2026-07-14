import re

def parse_log(log_line):
    pattern = r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\]\s+"(\w+)\s+(.*?)\s+HTTP.*?"\s+(\d+)'

    match = re.match(pattern, log_line)

    if match:
        return {
            "ip": match.group(1),
            "timestamp": match.group(2),
            "method": match.group(3),
            "url": match.group(4),
            "status": int(match.group(5))
        }

    return None