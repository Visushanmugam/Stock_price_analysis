""" Data Calculation Libraries """
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data

data = pd.read_csv("data_yahoo.csv", index_col="Date", parse_dates=True)

# Eur/Inr Moving Average One Day

plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="EUR/INR Colsing Price", color='black') # Ploting EUR/INR Closing Price pylint: disable=line-too-long
plt.plot(data["Close"].rolling(window=2).mean(), label="One Day Moving Averages", color='blue') # Ploting EUR/INR One Day Moving Averages pylint: disable=line-too-long
buy = np.where((data['Close'] > data["Close"].rolling(window=2).mean()) & (data['Close'].shift(1) < data["Close"].rolling(window=2).mean().shift(1)), 1, np.nan) * 0.95 * data['Low'] # pylint: disable=line-too-long
sell = np.where((data["Close"].rolling(window=2).mean() > data['Close']) & (data["Close"].rolling(window=2).mean().shift(1) < data['Close'].shift(1)), 1, np.nan) * 0.95 * data['High'] # pylint: disable=line-too-long
plt.scatter(data.index, buy, color='green', marker='^', label='Buy Signal') # Scatter EUR/INR Buy
plt.scatter(data.index, sell, color='red', marker='v', label='Sell Signal') # Scatter EUR/INR Sell
plt.title("EUR/INR Moving Averages One Day")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.legend()
plt.show()

# Eur/Inr Moving Average One Week

plt.plot(data["Close"], label="EUR/INR Colsing Price", color='black') # Ploting EUR/INR Closing Price pylint: disable=line-too-long
plt.plot(data["Close"].rolling(window=7).mean(), label="One Week Moving Averages", color='blue')
buy = np.where((data['Close'] > data["Close"].rolling(window=7).mean()) & (data['Close'].shift(1) < data["Close"].rolling(window=7).mean().shift(1)), 1, np.nan) * 0.95 * data['Low'] # pylint: disable=line-too-long
sell = np.where((data["Close"].rolling(window=7).mean() > data['Close']) & (data["Close"].rolling(window=7).mean().shift(1) < data['Close'].shift(1)), 1, np.nan) * 0.95 * data['High'] # pylint: disable=line-too-long
plt.scatter(data.index, buy, color='green', marker='^', label='Buy Signal') # Scatter EUR/INR Buy
plt.scatter(data.index, sell, color='red', marker='v', label='Sell Signal') # Scatter EUR/INR Sell
plt.title("EUR/INR Moving Averages One Week")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.legend()
plt.show()

# EUR/INR Bolinger Band One Day

plt.plot(data["Close"], label="EUR/INR Colsing Price", color='black') # Ploting EUR/INR Closing Price pylint: disable=line-too-long
data['Std1'] = statistics.stdev(data["Close"])
plt.plot(data["Close"].rolling(window=2).mean(), label="Simple Moving Average", color='red') # Ploting EUR/INR Simple Moving Average pylint: disable=line-too-long
plt.plot(data["Close"].rolling(window=2).mean() + 2 * data['Std1'], label="Upper Band", color='blue') # Ploting EUR/INR Bolinger Upper Band One day pylint: disable=line-too-long
plt.plot(data["Close"].rolling(window=2).mean() - 2 * data['Std1'], label="Lower band", color='green') # Ploting EUR/INR Bolinger Upper Band One day pylint: disable=line-too-long
plt.title("EUR/INR Bolinger Band One Day")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.legend()
plt.show()

# EUR/INR Bolinger Band One Week

plt.plot(data["Close"], label="EUR/INR Colsing Price", color='black') # Ploting EUR/INR Closing Price pylint: disable=line-too-long
data['Std7'] = statistics.stdev(data["Close"])
plt.plot(data["Close"].rolling(window=7).mean(), label="Simple Moving Average", color='red') # Ploting EUR/INR Simple Moving Average pylint: disable=line-too-long
plt.plot(data["Close"].rolling(window=7).mean() + 2 * data['Std7'], label="Upper Band", color='blue') # Ploting EUR/INR Bolinger Upper Band One Week pylint: disable=line-too-long
plt.plot(data["Close"].rolling(window=7).mean() - 2 * data['Std7'], label="Lower band", color='green') # Ploting EUR/INR Bolinger Lower Band One Week pylint: disable=line-too-long
plt.title("EUR/INR Bolinger Band One Week")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.legend()
plt.show()


# EUR/INR CCI One Day


fig1, ax = plt.subplots(2, sharex=True)
data['typical_price'] = (data['Close'] + data['High'] + data['Low']) / 3
data["SMA"] = data["typical_price"].rolling(window=2).mean()
data["mean_deviation"] = np.abs(data['typical_price'] - data["SMA"]).rolling(window=2).mean()
data["cci"] = (data['typical_price'] - data["SMA"]) / (0.015 * data["mean_deviation"])
ax[0].plot(data["Close"], label="EUR/INR Colsing Price", color='black') # Ploting EUR/INR Closing Price pylint: disable=line-too-long
ax[0].legend(loc="upper left")
ax[1].plot(data["cci"], label="One Day CCI", color='blue') # Ploting EUR/INR One Day CCI
ax[1].legend(loc="upper left")
plt.suptitle("EUR/INR CCI One Day")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.show()

# EUR/INR CCI One Week

fig1, ax = plt.subplots(2, sharex=True)
data['typical_price'] = (data['Close'] + data['High'] + data['Low']) / 3
data["SMA"] = data["typical_price"].rolling(window=7).mean()
data["mean_deviation"] = np.abs(data['typical_price'] - data["SMA"]).rolling(window=7).mean()
data["cci"] = (data['typical_price'] - data["SMA"]) / (0.015 * data["mean_deviation"])
ax[0].plot(data["Close"], label="EUR/INR Colsing Price", color='black') # Ploting EUR/INR Closing Price pylint: disable=line-too-long
ax[0].legend(loc="upper left")
ax[1].plot(data["cci"], label="One Week CCI", color='blue') # Ploting EUR/INR One Week CCI
ax[1].legend(loc="upper left")
plt.suptitle("EUR/INR CCI One Week")
plt.xlabel("Date")
plt.ylabel("EUR/INR Stock Price")
plt.show()
