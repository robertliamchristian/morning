import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt

def fetch_daily_stock_data(symbol):
    url = "https://alpha-vantage.p.rapidapi.com/query"
    querystring = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "outputsize": "compact",
        "datatype": "json"
    }
    headers = {
        "X-RapidAPI-Key": "d49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Check if 'Time Series (Daily)' key exists in the response
    if 'Time Series (Daily)' in data:
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df.reset_index(inplace=True)
        df.rename(columns={
            'index': 'Date',
            '1. open': 'Open',
            '2. high': 'High',
            '3. low': 'Low',
            '4. close': 'Close',
            '5. volume': 'Volume'
        }, inplace=True)
        df['Symbol'] = symbol
        return df
    else:
        print(f"No data for symbol: {symbol}")
        return pd.DataFrame()
    
def get_daily_stock_data():
    symbols = ['CNC', 'UHG', 'GCMG','CVS','CI','PFE','CRSP']
    all_data = []

    for symbol in symbols:
        stock_data = fetch_daily_stock_data(symbol)
        if not stock_data.empty:
            # Sort the DataFrame by date and get the top 3 rows for the symbol
            top_3_data = stock_data.sort_values(by='Date', ascending=False).head(3)
            all_data.append(top_3_data)

    if not all_data:
        print("No data to concatenate")
        return pd.DataFrame()
    else:
        combined_df = pd.concat(all_data)

    # Select only the 'Date', 'Close', and 'Symbol' columns
    combined_df = combined_df[['Date', 'Close', 'Symbol']]

    return combined_df