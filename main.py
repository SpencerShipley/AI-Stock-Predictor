from keras.layers import LSTM, Dense
from keras.models import Sequential
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

ticker = (input("REMINDER: Stock tickers are case sensitive\nEnter a stock ticker: "))

if ticker == "AAPL":
    csv_data = np.loadtxt('CSV/AAPL.csv', delimiter=',')
elif ticker == "AMZN":
    csv_data = np.loadtxt('CSV/AMZN.csv', delimiter=',')
elif ticker == "CVS":
    csv_data = np.loadtxt('CSV/CVS.csv', delimiter=',')
elif ticker == "GOOG":
    csv_data = np.loadtxt('CSV/GOOG.csv', delimiter=',')
elif ticker == "MCD":
    csv_data = np.loadtxt('CSV/MCD.csv', delimiter=',')
elif ticker == "UNH":
    csv_data = np.loadtxt('CSV/UNH.csv', delimiter=',')
elif ticker == "WMT":
    csv_data = np.loadtxt('CSV/WMT.csv', delimiter=',')
elif ticker == "XOM":
    csv_data = np.loadtxt('CSV/XOM.csv', delimiter=',')
else:
    print("ERROR. Ticker entered is either not a part of this program or entered incorrectly. "
          "Please restart the program and try again.")

closing_prices = csv_data[:, 4]

timesteps = 5
x = []
y = []
for i in range(timesteps, len(closing_prices)):
     x.append(closing_prices[i - timesteps:i])
     y.append(closing_prices[i])
x = np.array(x)
y = np.array(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

model = Sequential()
model.add(LSTM(units=1150, input_shape=(x_train.shape[1], x_train.shape[2])))
model.add(Dense(1))

model.compile(loss='mean_squared_error', optimizer='Adam')

model.fit(x_train, y_train, epochs=250, batch_size=32, validation_data=(x_test, y_test))

predictions = model.predict(x_test)

recent_data = closing_prices[-timesteps:]

recent_data = np.reshape(recent_data, (1, timesteps, 1))

prediction = model.predict(recent_data)[0]

print("Prediction:", prediction)

last_days_close = closing_prices[-1]

if prediction > last_days_close:
    print("Prediction:", prediction, "Last close:", last_days_close, "BUY!")
else:
    print("Prediction:", prediction, "Last close:", last_days_close, "DO NOT BUY. This stock is not expected to increase.")

