from pandas_datareader._utils import RemoteDataError
from pandas_datareader import data
import pandas as pd
import numpy as np
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
week_ago = '2020-07-27'

stocks_list = open('stocks.txt', 'r')
output = open('output.txt', 'w')

def clean_data(stock_data, row):
  weekdays = pd.date_range(start=week_ago, end=today)
  clean_data = stock_data[row].reindex(weekdays)
  return clean_data.fillna(method='ffill')

def get_data(stock_code):
  try:
    stock_data = data.DataReader(stock_code, 'yahoo', week_ago, today)
    output.write('-------------- ' + stk + ' --------------\n')
    output.write(str(clean_data(stock_data, 'High')) + '\n')
    output.write(str(clean_data(stock_data, 'Low')) + '\n')
    output.write(str(clean_data(stock_data, 'Close')) + '\n')
  except RemoteDataError:
    print('No data found for ' + stock_code)

for stock in stocks_list:
  stk = stock.replace('\n', '')
  get_data(stk + '.sa')