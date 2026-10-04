import pandas as pd
from emailAlert import sendEmailAlert

trafficDf = pd.read_csv('data/dailyPerformance.csv')

trafficDf['Date'] = pd.to_datetime(trafficDf['Date'])

sortedDate= (
    trafficDf.sort_values(by='Date', ascending=True)
)

# Current Period
latestDate = sortedDate['Date'].max()
currentStartDate = latestDate - pd.Timedelta(days=6)

currentPeriodDf = (
    sortedDate[
        (sortedDate['Date'] >= currentStartDate) &
        (sortedDate['Date'] <= latestDate)
    ]
)
# Previous Period
previousEndDate = currentStartDate - pd.Timedelta(days=1)
previousStartDate = previousEndDate - pd.Timedelta(days=6)

previousPeriodDf = (
    sortedDate[
        (sortedDate['Date'] >= previousStartDate) &
        (sortedDate['Date'] <= previousEndDate)
    ]
)

# Active Users
previousActiveUsers = previousPeriodDf['Active Users'].sum()
currentActiveUsers = currentPeriodDf['Active Users'].sum()
# Finding Active Users Percentage Change
activeUsersChange = round(((currentActiveUsers - previousActiveUsers) / previousActiveUsers) * 100, 1)

# Session 
previousSessions = previousPeriodDf['Sessions'].sum()
currentSessions = currentPeriodDf['Sessions'].sum()
# Finding Sessions Percentage Change 
sessionsChange = round(((currentSessions - previousSessions) / previousSessions) * 100, 1)

# New Users 
previousNewUsers = previousPeriodDf['New Users'].sum()
currentNewUsers = currentPeriodDf['New Users'].sum()
# Finding New Users Percentage Change
newUsersChange = round(((currentNewUsers - previousNewUsers)/ previousNewUsers) * 100, 1)

# Engagement 
previousEngagementRate = previousPeriodDf['Engagement Rate'].mean()
currentEngagementRate = currentPeriodDf['Engagement Rate'].mean()
# Finding Engagement Percentage Change
engagementRateChange = round(((currentEngagementRate - previousEngagementRate) / previousEngagementRate) * 100, 1)

comparisonDf = pd.DataFrame({
    'Metric': ['Active Users', 'Sessions', 'New Users', 'Engagement Rate'],
    'Previous': [previousActiveUsers, previousSessions, previousNewUsers, previousEngagementRate],
    'Current': [currentActiveUsers, currentSessions, currentNewUsers, currentEngagementRate],
    'Change (%)': [activeUsersChange, sessionsChange, newUsersChange, engagementRateChange]
})
comparisonDf['Date Run'] = latestDate
comparisonDf.to_csv('data/MonitoringReport.csv', index=False)

# Monitoring Rules - Testing
alerts = []

# Active Users Validation
if currentActiveUsers < previousActiveUsers:
    alerts.append(f'Alert: Active Users are lower than expected. Previous: {previousActiveUsers}, Current: {currentActiveUsers}')

# Sessions Validation 
if currentSessions < previousSessions:
    alerts.append(f'Alert: Sessions are lower than expected. Previous: {previousSessions}, Current: {currentSessions}')

# New Users Validation
if currentNewUsers < previousNewUsers:
    alerts.append(f'Alert: New Users are lower than expected. Previous: {previousNewUsers}, Current: {currentNewUsers}')

# Engagement Rate Validation
if currentEngagementRate < previousEngagementRate:
    alerts.append(f'Alert: Engagement Rate is lower than expected. Previous: {previousEngagementRate:.1%}, Current: {currentEngagementRate:.1%}')

alertMessage = '\n\n'.join(alerts)

if len(alerts) > 0:
    print(alertMessage)
    sendEmailAlert(alertMessage)
else:
    print('No traffic drops detected.')