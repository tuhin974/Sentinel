from src.tailer import tail_file
from src.parser import parse_log
from src.features import extract_features
from src.detector import predict_anomaly
from src.logger import logger
from src.config import load_config
from src.alert import send_slack_alert

config = load_config()

LOG_FILE = config["log_file"]

logger.info("====================================")
logger.info("Sentinel started")
logger.info(f"Monitoring log file: {LOG_FILE}")

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
        logger.warning("Invalid log format received.")
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

        logger.warning(
            f"Anomaly detected | IP={parsed_data['ip']} | "
            f"Method={parsed_data['method']} | "
            f"URL={parsed_data['url']} | "
            f"Status={parsed_data['status']}"
        )

        send_slack_alert(parsed_data)

        print("🚨 ANOMALY DETECTED")
        print("📩 Slack notification sent.")

    else:

        logger.info(
            f"Normal request | IP={parsed_data['ip']} | "
            f"Method={parsed_data['method']} | "
            f"URL={parsed_data['url']} | "
            f"Status={parsed_data['status']}"
        )

        print("✅ Normal Request")