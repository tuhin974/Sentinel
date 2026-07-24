import requests

from src.config import load_config

config = load_config()

WEBHOOK_URL = config["slack_webhook"]


def send_slack_alert(parsed_data):
    """
    Send anomaly alert to Slack.
    """

    message = {
        "text":
        f"""
🚨 *Sentinel Alert*

*Anomaly Detected!*

IP: {parsed_data['ip']}
Method: {parsed_data['method']}
URL: {parsed_data['url']}
Status: {parsed_data['status']}
Time: {parsed_data['timestamp']}
"""
    }

    response = requests.post(
        WEBHOOK_URL,
        json=message
    )

    return response.status_code