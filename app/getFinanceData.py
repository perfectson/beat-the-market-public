import yfinance as yf
import pandas as pd
import re 
import pathlib
import os, glob
equities_folder_path = "/workspace/beat-the-market-public/test_data/equities/" 

def getStockData():
    index_members = pd.read_csv('/workspace/beat-the-market-public/test_data/sp500.csv', index_col=0, parse_dates=[0])

    #today = zipline.api.get_datetime()
    
    # Second, get the index makeup for all days prior to today.
    
    
    # Now let's snag the first column of the last, i.e. latest, entry.
    #for i in index_members
    for i in range(len(index_members)):

        latest_day = index_members.iloc[i,0]

        # Split the text string with tickers into a list
        list_of_tickers = latest_day.split(',')
        print(len(index_members))
        for ticker in list_of_tickers:
            ticker = "".join(re.split("[^a-zA-Z]*", ticker)) 
            #print(ticker)
            if (pathlib.Path("/workspace/beat-the-market-public/test_data/equities/"+ticker+".csv").exists()):
                print(ticker +" already stored")
            else:
                ticker_hist = yf.Ticker(ticker).history(period="max") 
                print(ticker_hist)
                if len(ticker_hist) > 2:
                    ticker_hist.columns=["open","high","low","close","volume","dividends","splits"]
                    ticker_hist.index.names=["date"]
                    ticker_hist.to_csv (r'/workspace/beat-the-market-public/test_data/equities/'+ ticker +'.csv', index = True, header=True)


def getNyseData():
    index_members = pd.read_csv('/workspace/beat-the-market-public/test_data/components/NYSE.csv', header=0)

    #today = zipline.api.get_datetime()
    
    # Second, get the index makeup for all days prior to today.
    
    print(index_members)
    # Now let's snag the first column of the last, i.e. latest, entry.

    for i in range(len(index_members)):

        ticker = index_members.iloc[i,0]

        if (pathlib.Path("/workspace/beat-the-market-public/test_data/equities/"+ticker+".csv").exists()):
            print(ticker +" already stored")
        else:
            ticker_hist = yf.Ticker(ticker).history(period="max") 
            #print(ticker_hist)
            if len(ticker_hist) > 2:
                ticker_hist.columns=["open","high","low","close","volume","dividends","splits"]
                ticker_hist.index.names=["date"]
                ticker_hist.to_csv (r'/workspace/beat-the-market-public/test_data/equities/'+ ticker +'.csv', index = True, header=True)

   
def getEmptyFile():

    csv = pathlib.Path(equities_folder_path).glob("*.csv")
    for fi in csv:
#        print(fi)

        #full_file_path = equities_folder_path + sym + ".csv"
#        data = pd.read_csv(fi, index_col=0, parse_dates=['Date'])
        data = pd.read_csv(fi, index_col=0, parse_dates=True)
        if len(data) < 2:
            #os.remove(fi)
            print(fi + " empty")

def changeHeaderToZiplineBundle():
    csv = pathlib.Path(equities_folder_path).glob("*.csv")
    for fi in csv:
        df = pd.read_csv(fi, index_col=0, parse_dates=True)
        if(len(df.columns)==7):
            df.columns=["open","high","low","close","volume","dividends","splits"]
            df.index.names=["date"]

            df.to_csv (fi, index = True, header=True)        #new_header = df.iloc[1] #grab the first row for the header
#        print(new_header)Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
        #df = df[1:] #take the data less the header row
#
        print(df)

def removeEmpytfiles(folder_path):
    os.chdir(folder_path)
    for fi in glob.glob("*.csv"):
        
        data = pd.read_csv(fi, index_col=0, parse_dates=True)
        if len(data) < 2:
            os.remove(fi)
            print(fi + " removed")
       # os.remove(fi)  

getNyseData()
#removeEmpytfiles(equities_folder_path)
#changeHeaderToZiplineBundle()
#getStockData()
#getEmptyFile()
