from src.tailer import tail_file
from src.parser import parse_log
from src.features import extract_features
from src.detector import predict_anomaly

LOG_FILE = "logs/sample.log"

print("====================================")
print(" Sentinel - Real-Time Log Monitor")
print("====================================")
print(f"Monitoring: {LOG_FILE}")
print("Waiting for new log entries...\n")

for log_line in tail_file(LOG_FILE):

    if not log_line.strip():
        continue

    parsed_data = parse_log(log_line)

    if parsed_data is None:
        print("⚠️ Invalid log format")
        continue

    features = extract_features(parsed_data)

    prediction = predict_anomaly(features)

    print("\n========== NEW LOG ==========")
    print(log_line)

    print("\nParsed Data:")
    print(parsed_data)

    print("\nExtracted Features:")
    print(features)

    print("\nPrediction:")

    if prediction == -1:
        print("🚨 ANOMALY DETECTED")
    else:
        print("✅ Normal Request")