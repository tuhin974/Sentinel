from datetime import datetime


class AlertManager:

    def send_alert(self, log_message, score):

        print("\n" + "=" * 60)
        print("🚨 SENTINEL ALERT")
        print("=" * 60)
        print(f"Time      : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Log       : {log_message}")
        print(f"Score     : {score:.4f}")
        print("=" * 60 + "\n")