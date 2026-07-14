import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.parser import parse_log

log = '127.0.0.1 - - [15/Jul/2026:10:01:12] "GET /login HTTP/1.1" 200'

result = parse_log(log)

print(result)