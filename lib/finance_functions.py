import numpy as np
import pandas as pd
"""
create function to change settings
"""
# Settings
window = 126
year_length = 252

# Function for annualized return
def ann_ret(ts):
    return np.power((ts[-1] / ts[0]), (year_length/len(ts))) -1 

# Function for drawdown
def dd(ts):
    return np.min(ts / np.maximum.accumulate(ts)) - 1