import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tailer import tail_file

print("Sentinel Started...")
print("Monitoring logs/sample.log")
print("Press Ctrl+C to stop.\n")

tail_file("logs/sample.log")