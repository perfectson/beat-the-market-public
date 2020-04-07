import pandas as pd
import matplotlib.pyplot as plt

# Read data from csv
df = pd.read_csv('test_data/oil_etf_vs_spot.csv', index_col='Date', parse_dates=['Date'])

# Make  new figure and set the size.
fig = plt.figure(figsize=(12, 8))

# The first subplot, planning for 3 plots high, 1 plot wide, this being the first.
ax = fig.add_subplot(111)
ax.set_title('Oil ETF vs. Spot')
ax.plot(df['WTI-West-Texas-Intermediate'], linestyle='-', label='Spot', linewidth=3.0, color='black')
ax.plot(df['USO'], linestyle='--', label='ETF', linewidth=3.0, color = 'grey')
ax.legend()
