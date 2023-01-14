# AI-Stock-Predictor

This project uses a Long Short Term Neural Network to predict a stock's next day closing price. Data is updated to 01/04/2023. The overarching goal of this project was
to see how accurate a machine learning model could predict stock prices. 

Important things to note about this project:
The project is built in Python using an LSTM.
The data is sourced directly from Yahoo Finance and stored in CSV files
The data includes daily opening prices, highs, lows, closing prices, adjusted closing prices, and trading volume HOWEVER, only the closing prices are used. 
The model uses the AAPL, AMZN, CVS, GOOG, MCD, UNH, WMT, and XOM stock tickers. 
The model is more accurate for lower stock prices ($80-$150 range).
The closest prediction I achieved on the day was on 12/29/2022. The model predicted AMZN's next day closing price within 6 cents!
The least accurate prediction was on 12/29/2022. The model predicted UNH's closing price within $27.45. 
I tested every trading day from 12/29/2022-01/04/2023. I have not tested since. 
On the days tested, it correctly predicted the direction of the stock's price (up or down) 49.1%. 
