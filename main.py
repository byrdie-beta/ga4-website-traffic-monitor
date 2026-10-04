from dailyPerformance import getDailyPerformance
import pandas as pd

dailyDf = getDailyPerformance()

dailyDf['Date'] = pd.to_datetime(dailyDf['Date'], format='%Y%m%d')
dailyDf.to_csv('data/dailyPerformance.csv', index=False)