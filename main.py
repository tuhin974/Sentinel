import time
from src.tailer import LogTailer
from src.parser import parse_log
from src.features import extract_features
from src.detector import LogDetector
from src.logger import logger
from src.config import load_config
from src.alert import send_slack_alert

config = load_config()
detector = LogDetector()

LOG_FILE = config["log_file"]

start_time = time.time()

processed_logs = 0
normal_logs = 0
anomaly_logs = 0
slack_alerts = 0

logger.info("====================================")
logger.info("Sentinel started")
logger.info(f"Monitoring log file: {LOG_FILE}")

print("====================================")
print(" Sentinel - Real-Time Log Monitor")
print("====================================")
print(f"Monitoring: {LOG_FILE}")
print("Waiting for new log entries...\n")

tailer = LogTailer(LOG_FILE)

for log_line in tailer.follow():

    if not log_line.strip():
        continue
    processed_logs += 1

    parsed_data = parse_log(log_line)

    if parsed_data is None:
        logger.warning("Invalid log format received.")
        print("⚠️ Invalid log format")
        continue

    features = extract_features(parsed_data)

    prediction, score = detector.predict(log_line)

    if prediction == "ANOMALY":
        confidence = min(90 + abs(score) * 100, 99.9)
    else:
        confidence = min(70 + max(score, 0) * 100, 99.9)


    print("\n" + "=" * 60)
    print("🛡️ Sentinel - Real-Time Log Anomaly Detector")
    print("=" * 60)

    print(f"IP Address : {parsed_data['ip']}")
    print(f"Timestamp  : {parsed_data['timestamp']}")
    print(f"Method     : {parsed_data['method']}")
    print(f"URL        : {parsed_data['url']}")
    print(f"Status     : {parsed_data['status']}")

    print("\nPrediction")
    print("-" * 20)
    print(f"Score      : {score:.4f}")
    print(f"Confidence : {confidence:.1f}%")


    if prediction == "ANOMALY":
        anomaly_logs += 1
        logger.warning(
            f"Anomaly detected | IP={parsed_data['ip']} | "
            f"Method={parsed_data['method']} | "
            f"URL={parsed_data['url']} | "
            f"Status={parsed_data['status']}"
        )

        send_slack_alert(parsed_data)
        slack_alerts += 1

        print("Prediction : 🚨 ANOMALY")
        print("Slack      : Sent ✅")

    else:
        normal_logs += 1
        logger.info(
            f"Normal request | IP={parsed_data['ip']} | "
            f"Method={parsed_data['method']} | "
            f"URL={parsed_data['url']} | "
            f"Status={parsed_data['status']}"
        )

        print("Prediction : ✅ NORMAL")

        elapsed = int(time.time() - start_time)

        hours = elapsed // 3600
        minutes = (elapsed % 3600) // 60
        seconds = elapsed % 60

        print("\n====================================")
        print("📊 Sentinel Dashboard")
        print("====================================")
        print(f"Processed Logs : {processed_logs}")
        print(f"Normal Logs    : {normal_logs}")
        print(f"Anomalies      : {anomaly_logs}")
        print(f"Slack Alerts   : {slack_alerts}")
        print(f"Uptime         : {hours:02}:{minutes:02}:{seconds:02}")
        print("====================================")