import pandas as pd
data = pd.read_csv('./assignments/nycflights13.csv.bz2', '\t')
delay = data.mean(axis=0, skipna=True).arr_delay
print(delay)