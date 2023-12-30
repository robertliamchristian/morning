import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime
from datetime import datetime as dt

def fetch_calendar_events(api_key, calendar_id2):
    url = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"
    current_date = datetime.date.today()
    start_of_day = datetime.datetime.combine(current_date, datetime.time())
    end_of_day = datetime.datetime.combine(current_date, datetime.time(23, 59, 59))
    params = {
        'key': api_key,
        'timeMin': start_of_day.isoformat() + 'Z',
        'timeMax': end_of_day.isoformat() + 'Z',
        'singleEvents': True,
        'orderBy': 'startTime'
    }
    response = requests.get(url, params=params)
    events = response.json().get('items', [])
    data = [{'Name': event['summary'], 
             'Start': event['start'].get('dateTime', event['start'].get('date')), 
             'End': event['end'].get('dateTime', event['end'].get('date'))} 
            for event in events]
    df = pd.DataFrame(data)
    if df.empty:
        # If it is, create a new DataFrame with a single row containing your message
        df = pd.DataFrame([{'Name': 'No Calendar Results Today', 'Start': '', 'End': ''}])
    return df
