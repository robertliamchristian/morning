import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt
from weather import fetch_weather
from my_calendar import fetch_calendar_events
from morning_dates import morning_update_dates
from get_random import get_random_food, get_random_tasks, get_random_turkish_quote, get_random_affirmation
from stock import get_daily_stock_data
#from get_soccer import fetch_football_odds
from ny_flights import fetch_ny_flights
from cy_flights import fetch_cy_flights
from ar_flights import fetch_ar_flights
from npr import get_npr_data





def render_template(context):
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('morning_update.html')
    return template.render(context)


def morning_update(weather_api_key, calendar_api_key, calendar_id, football_api_key):
    # Fetch weather data
    temp, weather_description, temp_high, temp_low, sunrise, sunset = fetch_weather(weather_api_key)
    # Fetch soccer data
    #football_odds_data = fetch_football_odds(football_api_key)
    # Fetch calendar events
    calendar_events = fetch_calendar_events(calendar_api_key, calendar_id)
    l_calendar_events = fetch_calendar_events(calendar_api_key, calendar_id2)
    # Fetch stock data
    daily_stock_data = get_daily_stock_data()
    # Fetch date information
    today_date, days_new_year, days_birthday, days_lindsay_birthday = morning_update_dates()
    food_recommendations = get_random_food()
    task_recommendations = get_random_tasks()
    turkish_quote, english_translation = get_random_turkish_quote()
    affirmation = get_random_affirmation()
    ny_flights_data = fetch_ny_flights()  # Call the function to get the DataFrame
    ny_flights_html = ny_flights_data.to_html(index=False, classes='flights-table')
    cy_flights_data = fetch_cy_flights()
    cy_flights_html = cy_flights_data.to_html(index=False, classes='flights-table')
    ar_flights_data = fetch_ar_flights()
    ar_flights_html = ar_flights_data.to_html(index=False, classes='flights-table')
    npr_data = get_npr_data()
    npr_data_html = npr_data.to_html(index=False, classes='npr-table')  

    

    # Fetch news daa
    #news_data = fetch_news_data()

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
        #'football_odds_data': football_odds_data.to_html(index=False, classes='football-odds-table'),
        'food_for_today': food_recommendations,
        'task_for_today': task_recommendations,
        'daily_stock_data': daily_stock_data.to_html(index=False, classes='stock-table'),
        'turkish_quote': turkish_quote,
        'english_translation': english_translation,
        'calendar_events': calendar_events.to_html(index=False, classes='calendar-table'),
        'affirmation': affirmation,
        'ny_flights': ny_flights_html,
        'cy_flights': cy_flights_html,
        'ar_flights': ar_flights_html,
        'l_calendar_events': l_calendar_events.to_html(index=False, classes='calendar-table'),
        'npr_data': npr_data_html,
        
    }
        
    # Render the template
    rendered_html = render_template(context)
    with open('rendered_morning_update.html', 'w') as file:
        file.write(rendered_html)

    print("Good Morning, Robbie! Report is ready to refresh")

weather_api_key = '89fbedb87c83a9faf12a1319c4df142e'
calendar_api_key = 'AIzaSyBfw_KuFQwYvCgIm9ZDdJGuvqAKUWzmw5Q'
calendar_id = 'robertliamchristian@gmail.com'
calendar_id2 = 'lindsay.hooker@gmail.com'
football_api_key = 'd49e56dcbemsh75dcc891664b5a7p1cb502jsnaab489024d84'
morning_update(weather_api_key, calendar_api_key, calendar_id, football_api_key)

