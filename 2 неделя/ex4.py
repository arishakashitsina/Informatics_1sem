import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('BTC_data.csv')
data['time'] = pd.to_datetime(data['time']).dt.strftime('%d-%m-%Y')
data['close'] = pd.to_numeric(data['close'])
plt.figure(figsize=(12, 6))
plt.plot(data['time'], data['close'], label='BTC')
plt.grid()
plt.legend()
