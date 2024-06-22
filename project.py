'''using data processing'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Assume you have already fetched the historical data into a DataFrame called 'eur_inr_data'
# Columns: 'Date', 'Close' (EUR/INR closing price)
eur_inr_data = pd.read_csv("data_yahoo.csv")
# Calculate one-day moving average
eur_inr_data['OneDayMA'] = eur_inr_data['Close'].rolling(window=2).mean()

# Calculate one-week moving average
eur_inr_data['OneWeekMA'] = eur_inr_data['Close'].rolling(window=7).mean()

# Calculate Bollinger Bands
eur_inr_data['RollingStd'] = eur_inr_data['Close'].rolling(window=7).std()
eur_inr_data['UpperBand'] = eur_inr_data['OneWeekMA'] + 2 * eur_inr_data['RollingStd']
eur_inr_data['LowerBand'] = eur_inr_data['OneWeekMA'] - 2 * eur_inr_data['RollingStd']
plt.plot(eur_inr_data['Close'])
plt.plot(eur_inr_data['OneWeekMA'] + 2 * eur_inr_data['RollingStd'])
plt.plot(eur_inr_data['OneWeekMA'] - 2 * eur_inr_data['RollingStd'])
plt.legend()
plt.show()


# Calculate CCI
typical_price = (eur_inr_data['Close'] + eur_inr_data['High'] + eur_inr_data['Low']) / 3
mean_deviation = np.abs(typical_price - eur_inr_data['OneWeekMA']).rolling(window=20).mean()
cci = (typical_price - eur_inr_data['OneWeekMA']) / (0.015 * mean_deviation)
print(cci)

# Create a PowerPoint presentation with relevant slides
# Include charts, explanations, and interpretations for each metric.

# Save the DataFrame to a CSV file for reference
eur_inr_data.to_csv('eur_inr_analysis.csv', index=False)
