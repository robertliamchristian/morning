from datetime import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random

app = Flask(__name__)

def render_template(context):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('morning_update.html')
    return template.render(context)

def fetch_weather(api_key, lat=45.52, lon=-122.68):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'imperial'
    }
    response = requests.get(url, params=params)
    data = response.json()
    print("Weather API Response:", data)  # Debug print
    if 'main' in data and 'weather' in data:
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        # You need to add sunrise, sunset, temp_high, and temp_low here
        # If the API does not provide these directly, calculate or set defaults
        # For now, I'll set them to None
        temp_high = data['main'].get('temp_max', None)
        temp_low = data['main'].get('temp_min', None)
        # Convert Unix timestamps to human-readable times if available
        sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M') if 'sys' in data else None
        sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M') if 'sys' in data else None
        return temp, weather_description, temp_high, temp_low, sunrise, sunset
    else:
        print("Error fetching weather data")
        return None, None, None, None, None, None

def fetch_football_predictions(football_api_key):
    today_date = datetime.now().date().isoformat()
    url = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
    querystring = {"iso_date": today_date, "market": "classic"}
    headers = {
        "X-RapidAPI-Key": football_api_key,
        "X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()['data']
    print("Football API Response:", data)
    df = pd.DataFrame([{
        'Home Team': match['home_team'],
        'Away Team': match['away_team'],
        'Competition': match['competition_name'],
        'Status': match['status'],
        'Result': match['result'],
        'Start Date': match['start_date'],
        'Odds 1': match['odds'].get('1'),
        'Odds X': match['odds'].get('X'),
        'Odds 2': match['odds'].get('2'),
    } for match in data])
    return df

def morning_update_dates():
    today = datetime.now()
    today_formatted = today.strftime("%A, %B %d, %Y")
    new_years_day = datetime(today.year + 1, 1, 1)
    birthday = datetime(today.year, 2, 5)
    lindsay_birthday = datetime(today.year, 6, 6)
    if today > birthday:
        birthday = datetime(today.year + 1, 2, 5)
    if today > lindsay_birthday:
        lindsay_birthday = datetime(today.year + 1, 6, 6)
    days_until_new_years = (new_years_day - today).days
    days_until_birthday = (birthday - today).days
    days_until_lindsay_birthday = (lindsay_birthday - today).days
    return today_formatted, days_until_new_years, days_until_birthday, days_until_lindsay_birthday

def get_random_food():
    breakfast_options = ["protein shake", "protein bar"]
    lunch_options = ["Paris Baguette", "Subway", "sushi"]
    dinner_options = ["Paris Baguette", "Subway", "sushi", "Mexican", "fast food"]
    
    return {
        'breakfast': random.choice(breakfast_options),
        'lunch': random.choice(lunch_options),
        'dinner': random.choice(dinner_options)
    }

def get_random_tasks():
    task_options = ["clean litter", "walk", "meditate", "yoga", "play guitar", "call a friend", "send Lindsay flowers"]
    
    return {
        'task': random.choice(task_options)
    }

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
            # Sort the DataFrame by date and get the top 5 rows for the symbol
            top_5_data = stock_data.sort_values(by='Date', ascending=False).head(3)
            all_data.append(top_5_data)

    combined_df = pd.concat(all_data)
    return combined_df

def morning_update(weather_api_key, football_api_key):
    # Fetch weather data
    temp, weather_description, temp_high, temp_low, sunrise, sunset = fetch_weather(weather_api_key)
    # Fetch football matches data
    football_data = fetch_football_predictions(football_api_key)
    # Fetch stock data
    daily_stock_data = get_daily_stock_data()
    # Fetch date information
    today_date, days_new_year, days_birthday, days_lindsay_birthday = morning_update_dates()
    food_recommendations = get_random_food()
    task_recommendations = get_random_tasks()
    
    # Adjust the context for the template
    context = {
        'temp': temp,
        'weather_description': weather_description,
        'temp_high': temp_high,
        'temp_low': temp_low,
        'sunrise': sunrise,
        'sunset': sunset,
        'today_date': today_date,
        'days_new_year': days_new_year,
        'days_birthday': days_birthday,
        'days_lindsay_birthday': days_lindsay_birthday,
        'matches_data': football_data.to_dict(orient='records'),  # Convert DataFrame to list of dicts
        'food_for_today': food_recommendations,
        'task_for_today': task_recommendations,
        'daily_stock_data': daily_stock_data.to_html(index=False, classes='stock-table')
    }
    # Render the template
    rendered_html = render_template(context)
    with open('rendered_morning_update.html', 'w') as file:
        file.write(rendered_html)

    print("Good Morning, Robbie! Report is ready to refresh")

    



weather_api_key = '89fbedb87c83a9faf12a1319c4df142e'
football_api_key = 'd49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84'
morning_update(weather_api_key, football_api_key)
