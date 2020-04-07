"""
need to create ac_equities_db, after delete this comment
"""
#%matplotlib inline
import zipline
from zipline.api import order_target_percent, symbol, schedule_function, date_rules, time_rules,order, record
from datetime import datetime
import pytz
from matplotlib import pyplot as plt
import pandas as pd
from collections import OrderedDict

etf = ["SPY","DBC","GLD","IEF","TLT"]
etf_folder_path = "/workspace/beat-the-market-public/test_data/ETF/" 

data = OrderedDict()
for sym in etf:
    full_file_path = etf_folder_path + sym + ".csv"
    data[sym] = pd.read_csv(full_file_path, index_col=0, parse_dates=['Date'])
    data[sym] = data[sym][["Open","High","Low","Close","Volume"]]
    #data[sym] = data[sym].resample("1d").mean()
    #data[sym].fillna(method="ffill", inplace=True)


    print(data[sym].head())

panel = pd.Panel(data)
panel.minor_axis = ["open","high","low","close","volume"]
panel.major_axis = panel.major_axis.tz_localize(pytz.utc)
print(panel["TLT"])

def initialize(context):
    context.securities = {
        'SPY': 0.25,
        'TLT': 0.3,
        'IEF': 0.3,
        'GLD': 0.075,
        'DBC': 0.075
    }
    #set_benchmark(symbol("SPY"))
    # Schedule rebalance for once a month
    schedule_function(rebalance, date_rules.month_start(), time_rules.market_open())
"""
def handle_data(context, data):
    order(symbol("SPY"), 10)
    record(SPY=data.current(symbol('SPY'), 'price'))
"""
def rebalance(context, data):
    # Loop through the securities
    for sec, weight in context.securities.items():
        sym = symbol(sec)
        # Check if we can trade
        if data.can_trade(sym):
            # Reset the weight
            order_target_percent(sym, weight)

# Set start and end
start = datetime(2007, 1, 1, 8, 15, 12, 0, pytz.UTC)
end = datetime(2018, 12, 31, 8, 15, 12, 0, pytz.UTC)

# Fire off backtest
result = zipline.run_algorithm(
    start=start, # Set start
    end=end, # Set end
    initialize=initialize, # Define startup function
    capital_base=100000, # Set initial capital
    data_frequency = 'daily', # Set data frequency
    data = panel ) # Select bundle

print("Ready to analyze result.")