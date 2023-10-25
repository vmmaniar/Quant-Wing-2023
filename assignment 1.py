import numpy as np
import pandas as pd
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import norm



def find_min_cov_stocks(cov_matrix):
  """Finds the 5 stocks with the minimum sum of covariance with each other.

  Args:
    cov_matrix: A numpy array representing the covariance matrix.

  Returns:
    A list of 5 stock tickers with the minimum sum of covariance with each other.
  """

  # Calculate the sum of covariances between each pair of stocks.
  cov_sum = np.sum(cov_matrix, axis=1)

  # Find the 5 pairs of stocks with the lowest sum of covariances.
  min_cov_pairs = np.argsort(cov_sum)[:5]

  # Get the stock tickers for the 5 pairs of stocks with the lowest sum of covariances.
  min_cov_stocks = []
  for pair in min_cov_pairs:
    min_cov_stocks.append(cov_matrix.index[int(pair[0])])
    min_cov_stocks.append(cov_matrix.index[int(pair[1])])

  # Return the list of 5 stock tickers with the minimum sum of covariance with each other.
  return min_cov_stocks



### Set time from to a certain number of years
years = 15

endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 365*years)

### Create a list of tickers
tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS', 'SBIN.NS', 'HINDUNILVR.NS', 'KOTAKBANK.NS', 'LT.NS', 'ADANIENTERPRISES.NS', 'BAJAJFINSV.NS', 'NESTLEIND.NS', 'HDFCLIFE.NS', 'ITC.NS', 'WIPRO.NS', 'BAJAJAUTO.NS', 'BHARTIARTL.NS', 'AXISBANK.NS', 'TECHM.NS', 'TITAN.NS', 'HINDALCO.NS']

### Download the daily adjusted close prices for the tickers
adj_close_df = pd.DataFrame()

for ticker in tickers:
    data = yf.download(ticker, start = startDate, end = endDate)
    adj_close_df[ticker] = data['Adj Close']

### Create a covariance matrix for all the securities
cov_matrix = adj_close_df.cov()
cov_matrix = np.array(cov_matrix)

min_cov_stocks = find_min_cov_stocks(cov_matrix)

print(min_cov_stocks)  
cov_sum = np.sum(cov_matrix, axis=1)
min_cov_pairs = np.argsort(cov_sum)[:5]
min_cov_stocks = []
for pair in min_cov_pairs:
    min_cov_stocks.append(cov_matrix.index[pair[0]])
    min_cov_stocks.append(cov_matrix.index[pair[1]])
return min_cov_stocks
