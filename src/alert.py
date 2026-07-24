import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load .env from project root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

WEBHOOK_URL = os.getenv("SLACK_WEBHOOK")


def send_slack_alert(parsed_data):
    """
    Send anomaly alert to Slack.
    """

    if not WEBHOOK_URL:
        print("⚠️ Slack webhook not configured.")
        return None

    message = {
        "text": f"""
🚨 *Sentinel Alert*

*Anomaly Detected!*

IP: {parsed_data['ip']}
Method: {parsed_data['method']}
URL: {parsed_data['url']}
Status: {parsed_data['status']}
Time: {parsed_data['timestamp']}
"""
    }

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=message,
            timeout=10
        )

        response.raise_for_status()
        return response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Slack Error: {e}")
        return None