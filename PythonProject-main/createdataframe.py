import pickle
import yfinance as yf

#Import tickers_used
filename = 'tickers_used'
infile = open(filename,'rb')
tickers_used = pickle.load(infile)
infile.close()

#Create string of tickers to pass through function
ticker_str = ''
for i in tickers_used:
    ticker_str = ticker_str + ' '+ i

#Create dataframe of historical prices for tickers_used
data = yf.download(ticker_str, start="2019-01-01", end="2019-04-01", interval= '1wk')['Close'].dropna()
#Store as a pickle
data.to_pickle('data')