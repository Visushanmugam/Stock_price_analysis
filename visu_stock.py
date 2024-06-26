import numpy as np
import pandas
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM


# Load Yahoo Data

data = pandas.read_csv('data_yahoo.csv')


# Prepare Data

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data['Close'].values.reshape(-1,1))

print(scaled_data)

predition_days = 60

x_train = []
y_train = []


for x in range(predition_days, len(scaled_data)):
    x_train.append(scaled_data[x-predition_days:x, 0])
    y_train.append(scaled_data[x, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build The Model

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1)) # Prediction of the next Closing Price

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=25, batch_size=32)

'''  Test The Model Accuracy on Existing Data'''

# Load Test Data

actual_price = data['Close'].values


total_dataset = pandas.concat((data['Close'], data['Close']), axis=0)


model_inputs = total_dataset[len(total_dataset) - len(data) - predition_days:].values

model_inputs = model_inputs.reshape(-1, 1)

model_inputs = scaler.transform(model_inputs)


# Make Predictions on Test Data

x_test = []

for x in range(predition_days, len(model_inputs)):
    x_test.append(model_inputs[x-predition_days:x, 0])


x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))


predicted_price = model.predict(x_test)
predicted_price = scaler.inverse_transform(predicted_price)


plt.plot(actual_price, color='black', label="Actual Stock Price")
plt.plot(predicted_price, color='blue', label="My Model Prediction Stock Price")
plt.xlabel('Time')
plt.ylabel('EUR/INR Share Price')
plt.title('EUR/INR Share Price')
plt.legend()
plt.show()



# Predict Futureday

real_data = [model_inputs[len(model_inputs) + 1 - predition_days:len(model_inputs+1), 0]]

real_data = np.array(real_data)

real_data = np.reshape(real_data, (real_data.shape[0], real_data.shape[1], 1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)

print(f"Model Prediction is {prediction}")
