from src.tailer import tail_file
from src.parser import parse_log
from src.features import extract_features

LOG_FILE = "logs/sample.log"

print("====================================")
print(" Sentinel - Real-Time Log Monitor")
print("====================================")
print(f"Monitoring: {LOG_FILE}")
print("Waiting for new log entries...\n")

for log_line in tail_file(LOG_FILE):

    # Skip empty lines
    if not log_line.strip():
        continue

    # Parse the log
    parsed_data = parse_log(log_line)

    # Skip invalid log format
    if parsed_data is None:
        print("\n⚠️ Invalid log format. Skipping...")
        continue

    # Extract features
    features = extract_features(parsed_data)

    print("\n========== NEW LOG ==========")
    print(log_line)

    print("\nParsed Data:")
    print(parsed_data)

    print("\nExtracted Features:")
    print(features)