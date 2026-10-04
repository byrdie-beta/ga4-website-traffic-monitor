#! python3
# emailAlert.py

from googleapiclient.discovery import build
from email.mime.text import MIMEText
import base64
from authentication import credentials


def sendEmailAlert(alertMessage):
    service = build('gmail', 'v1', credentials=credentials)

    message = MIMEText(alertMessage)
    message['to'] = 'you@example.com'  # Replace with your own email locally.
    message['subject'] = 'GA4 Website Traffic Alert'

    rawMessage = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId='me',
        body={'raw': rawMessage}
    ).execute()