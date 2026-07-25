from datetime import datetime
import os

import requests
from dotenv import load_dotenv


load_dotenv()


class AlertManager:
    def __init__(self):
        self.webhook_url = os.getenv("SLACK_WEBHOOK_URL")

    def send_alert(self, log_message, score):
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.console_alert(log_message, score, time)

        if self.webhook_url:
            self.slack_alert(log_message, score, time)

    def console_alert(self, log_message, score, time):
        print("\n" + "=" * 60)
        print("🚨 SENTINEL ALERT")
        print("=" * 60)
        print(f"Time  : {time}")
        print(f"Log   : {log_message}")
        print(f"Score : {score:.4f}")
        print("=" * 60 + "\n")

    def slack_alert(self, log_message, score, time):
        message = {
            "text": (
                "🚨 *SENTINEL SECURITY ALERT*\n"
                f"*Time:* {time}\n"
                f"*Log:* `{log_message}`\n"
                f"*Score:* {score:.4f}"
            )
        }

        try:
            response = requests.post(
                self.webhook_url,
                json=message,
                timeout=5
            )
            response.raise_for_status()
            print("Slack alert sent successfully.")

        except requests.RequestException as error:
            print(f"Slack alert failed: {error}")