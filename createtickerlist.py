import yahoo_fin.stock_info as si
import yfinance as yf
import pickle
import random


#Downloads all known tickers-- here we use a preexisting library for convenience
ticker_download = [si.tickers_dow(), si.tickers_other(), si.tickers_ftse100(), si.tickers_nasdaq(), si.tickers_niftybank(), si.tickers_ftse250(), si.tickers_ibovespa(), si.tickers_nifty50(), si.tickers_sp500()]

#Unpack, remove duplicates, alphabetize
ticker_list = [inner for outer in ticker_download for inner in outer]
ticker_list = list(set(ticker_list))
ticker_list.sort()

#Remove warrants, bonds, options, and all other non-equities
tickers = []
error_index = []
error_ticker = []
for i in ticker_list:
    try:
        print(len(tickers))
        print(i)
        #Check to see if the ticker corresponds to an industry, and is therefore a company
        if si.get_company_info(i).index.str.contains('industry').any() == True:
            tickers.append(i)
    #TypeErrors/KeyErrors appear if the ticker does not correspond to an industry, and is therefore not a company
    except (TypeError, KeyError, IndexError):
        #IndexErrors would sometimes glitch after like the 4th hour of running this code
        # ,in which case I decided to just manually inspect instead of running a recursive function
        if IndexError:
            error_index.append(tickers.index(i))
            error_ticker.append(i)
            pass
        else:
            pass

#Creating a library of the shares outstanding for each ticker
ticker_shares= {}
for ticker in tickers:
    #try to find the shares outstanding..
    try:
        print(ticker, tickers.index(ticker))
        ticker_shares[ticker] = yf.Ticker(ticker).info['sharesOutstanding']
    #... except assign None to the key's value
    except KeyError:
        ticker_shares[ticker] = None

#Rectroactively used this library as a second filter for the tickers list, due to some module idiosyncracies
for key in list(ticker_shares.keys()):
    if ticker_shares[key] == None:
        del ticker_shares[key]
        tickers.remove(key)


#Trim down list of tickers to ones that existed in 2018 onwards
tickers_2018 = tickers
remove = []
for i in tickers_2018:
    #try finding relevant data...
    try:
        print(i, tickers_2018.index(i))
        si.get_data(i,start_date="2018-01-05", end_date="2018-01-06")['close']
    #... except append ticker to remove list
    except (AssertionError, KeyError):
        remove.append(i)

#Remove all tickers from the remove list
for i in remove:
    tickers_2018.pop(tickers_2018.index(i))

#Randoml select 50 tickers to use
tickers_used = random.sample(tickers_2018, 50)

#Store tickers, tickers_2018, tickers_used objects to pickle files
filename = 'tickers'
outfile = open(filename, 'wb')
pickle.dump(tickers, outfile)
outfile.close()

filename = 'tickers_2018'
outfile = open(filename, 'wb')
pickle.dump(tickers, outfile)
outfile.close()

filename = 'tickers_used'
outfile = open(filename, 'wb')
pickle.dump(tickers, outfile)
outfile.close()
