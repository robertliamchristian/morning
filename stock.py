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
