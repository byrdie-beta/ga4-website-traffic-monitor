# GA4 Website Traffic Monitor

A Python project that collects daily Google Analytics 4 metrics, compares two seven-day periods, and sends a Gmail alert when metrics decline.

## Files

- `authentication.py`: signs in to Google and saves a local token for future runs.
- `dailyPerformance.py`: fetches the last 30 days of GA4 metrics through yesterday.
- `main.py`: saves the daily metrics to a CSV file.
- `trafficMonitor.py`: compares the latest seven days with the previous seven days and checks for declines.
- `emailAlert.py`: sends the alert through Gmail.

## Setup

Run commands from this project folder. Create a Python virtual environment and install the required packages:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p data
```

In your own Google Cloud project, enable the Google Analytics Data API and Gmail API, configure OAuth consent, and create OAuth credentials for a desktop application. Save the downloaded credentials as `credentials.json` in this folder. Your Google account needs access to the GA4 property and Gmail.

Before running, make these two edits in your local copy:

1. In `dailyPerformance.py`, replace `YOUR_GA4_PROPERTY_ID` with your GA4 property ID.
2. In `emailAlert.py`, replace `you@example.com` with your alert recipient.

Then run the fetch step followed by the monitoring step:

```sh
python main.py
python trafficMonitor.py
```

The first run opens a browser for Google sign-in. The project then saves `token.json` locally for later runs. Keep both JSON files private.

## Outputs

The project writes `data/dailyPerformance.csv` and `data/MonitoringReport.csv`. Alerts include metric values and are emailed to the recipient you configured. Credentials, tokens, and generated data are excluded from Git by `.gitignore`.

## Current limitations

Any decline in active users, sessions, new users, or average daily engagement rate triggers an alert. Engagement rate uses an unweighted average of daily values. Percentage changes may be undefined when a previous value is zero. The code does not append historical reports. Run the fetch step before monitoring, from this folder. Scheduling must be configured separately on your own computer.

## Changes for this public copy

The original five Python files and monitoring logic are retained. The personal property ID and email are replaced with placeholders. The unused Google Sheets permission is removed from the OAuth scopes. The missing Gmail client package (`google-api-python-client`) is added to the original dependency list. No extra configuration module is required.

Private credentials, tokens, analytics data, the virtual environment, and cached files are not included. The original working automation is separate and unchanged. This copy has passed Python syntax and private-value checks. Offline checks with synthetic data and simulated Google responses verified GA4 response parsing, CSV export, decline alerts, the no-alert case for growth, and Gmail message construction. These checks made no Google requests and sent no email. They used the existing local Python environment; a fresh dependency installation and live Google integration have not been tested.

Before publishing local edits, replace your property ID and email with the placeholders again. Never force-add ignored credentials or data to Git. Ignore rules do not remove files already committed.
