import yfinance as yf
import time

# Define a list of stocks to analyze
stocks = ['AAPL', 'GOOG', 'AMZN', 'NFLX', 'TSLA', 'META']

while True:
    # Retrieve the current market data for each stock
    data = yf.download(stocks, period='1d', interval='1m')['Close']

    # Calculate the daily percentage change for each stock
    pct_change = data.pct_change().fillna(0)

    # Calculate the mean and standard deviation of the percentage change for each stock
    mean = pct_change.mean()
    std = pct_change.std()

    # Identify stocks with a positive daily percentage change greater than 2 standard deviations from the mean
    trending_stocks = mean[mean > 0][std > 0][pct_change.iloc[-1] > mean + 2 * std].index.tolist()

    # Print the list of trending stocks
    print("Trending Stocks: ", trending_stocks)

    # Wait for 1 minute before retrieving the data again
    time.sleep(60)
