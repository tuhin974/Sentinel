from src.tailer import LogTailer
from src.detector import LogDetector
from src.alert import AlertManager


def main():
    tailer = LogTailer("logs/sample.log")
    detector = LogDetector()
    alert = AlertManager()

    for log in tailer.follow():
        if not log:
            continue

        label, score = detector.predict(log)

        print(f"{log} --> {label} ({score:.4f})")

        if label == "ANOMALY":
            alert.send_alert(log, score)


if __name__ == "__main__":
    main()