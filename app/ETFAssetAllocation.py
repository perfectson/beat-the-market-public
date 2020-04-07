"""
need to create ac_equities_db, after delete this comment
"""
#%matplotlib inline
import zipline
from zipline.api import order_target_percent, symbol, schedule_function, date_rules, time_rules
from datetime import datetime
import pytz
from matplotlib import pyplot as plt
import pandas as pd



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
    bundle = 'etf_bundle' ) # Select bundle

print("Ready to analyze result.")