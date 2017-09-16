import pandas as pd

#change 'dataset/dataset' to location of FB.csv on your computer
fbstock = pd.read_csv("datasets/datasets/FB.csv", parse_dates = True, index_col = 0)
fbstock["Close"].plot()

#change 90-day moving average to desiried time period in FB.csv dataset
pd.rolling_mean (fbstock["Close"], 90).plot()
