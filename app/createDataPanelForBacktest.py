

import pandas as pd
from collections import OrderedDict
import pytz

etf = ["SPY","DBC","GLD","IEF","TLT"]
etf_folder_path = "/workspace/beat-the-market-public/test_data/ETF/" 

data = OrderedDict()
for sym in etf:
    full_file_path = etf_folder_path + sym + ".csv"
    data[sym] = pd.read_csv(full_file_path, index_col=0, parse_dates=['Date'])
    data[sym] = data[sym][["Open","High","Low","Close","Volume"]]
    data[sym] = data[sym].resample("1d").mean()
    data[sym].fillna(method="ffill", inplace=True)

    print(data[sym].head())


panel = pd.Panel(data)
panel.minor_axis = ["open","high","low","close","volume"]
panel.major_axis = panel.major_axis.tz_localize(pytz.utc)
print(panel)
