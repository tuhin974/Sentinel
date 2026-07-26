from datetime import datetime
from pathlib import Path
import os

import requests
from dotenv import load_dotenv

from src.logger import logger


# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Support both environment-variable names
WEBHOOK_URL = (
    os.getenv("SLACK_WEBHOOK_URL")
    or os.getenv("SLACK_WEBHOOK")
)


class AlertManager:
    def __init__(self):
        self.webhook_url = WEBHOOK_URL

    def send_alert(self, log_message, score):
        alert_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.console_alert(log_message, score, alert_time)

        if self.webhook_url:
            self.slack_alert(log_message, score, alert_time)
        else:
            logger.warning("Slack webhook is not configured.")

    def console_alert(self, log_message, score, alert_time):
        print("\n" + "=" * 60)
        print("🚨 SENTINEL ALERT")
        print("=" * 60)
        print(f"Time  : {alert_time}")
        print(f"Log   : {log_message}")
        print(f"Score : {score:.4f}")
        print("=" * 60 + "\n")

    def slack_alert(self, log_message, score, alert_time):
        message = {
            "text": (
                "🚨 *SENTINEL SECURITY ALERT*\n"
                f"*Time:* {alert_time}\n"
                f"*Log:* `{log_message}`\n"
                f"*Score:* {score:.4f}"
            )
        }

        try:
            response = requests.post(
                self.webhook_url,
                json=message,
                timeout=10
            )
            response.raise_for_status()
            logger.info("Slack alert sent successfully.")

        except requests.RequestException as error:
            logger.error(f"Slack alert failed: {error}")


def send_slack_alert(parsed_data):
    """Send a backend parsed-log alert to Slack."""

    if not WEBHOOK_URL:
        logger.warning("Slack webhook is not configured.")
        return None

    message = {
        "text": (
            "🚨 *Sentinel Alert*\n\n"
            "*Anomaly Detected!*\n\n"
            f"IP: {parsed_data.get('ip', 'Unknown')}\n"
            f"Method: {parsed_data.get('method', 'Unknown')}\n"
            f"URL: {parsed_data.get('url', 'Unknown')}\n"
            f"Status: {parsed_data.get('status', 'Unknown')}\n"
            f"Time: {parsed_data.get('timestamp', 'Unknown')}"
        )
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=message,
            timeout=10
        )
        response.raise_for_status()
        logger.info("Backend Slack alert sent successfully.")
        return response.status_code

    except requests.RequestException as error:
        logger.error(f"Slack error: {error}")
        return None