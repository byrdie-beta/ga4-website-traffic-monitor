#! python3
# dailyPerformance.py

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest,
    DateRange,
    Dimension,
    Metric
)
import pandas as pd
from authentication import credentials

def getDailyPerformance():
    propertyId = "YOUR_GA4_PROPERTY_ID"  # Replace with your own property ID locally.
    client = BetaAnalyticsDataClient(
        credentials=credentials
        )

    request = RunReportRequest(
    property=f"properties/{propertyId}",
    dimensions=[
        Dimension(name="date"),
    ],
    metrics=[
        Metric(name="activeUsers"),
        Metric(name="sessions"),
        Metric(name="newUsers"),
        Metric(name="engagementRate"),
        Metric(name="keyEvents")
    ],
    date_ranges=[
        DateRange(
            start_date="30daysAgo",
            end_date="yesterday"
            )
        ]
    )
    response = client.run_report(request)

    dailyData = []

    for row in response.rows:
        dailyData.append({
        "Date": row.dimension_values[0].value,
        "Active Users": int(row.metric_values[0].value),
        "Sessions": int(row.metric_values[1].value),
        "New Users": int(row.metric_values[2].value),
        "Engagement Rate": float(row.metric_values[3].value),
        "Key Events": float(row.metric_values[4].value)
    })

    dailyPerformanceDf = pd.DataFrame(dailyData)
    return dailyPerformanceDf

