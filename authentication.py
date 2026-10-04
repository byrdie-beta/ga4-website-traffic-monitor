#! python3
# authentication.py

import pandas as pd 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
import os
from google.auth.transport.requests import Request

scopes = [
    "https://www.googleapis.com/auth/analytics.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",
    scopes
)

if os.path.exists('token.json'):
    credentials = Credentials.from_authorized_user_file(
        'token.json',
        scopes
    )

    if credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

else:
    credentials = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(credentials.to_json())

print("Authentication successful!")