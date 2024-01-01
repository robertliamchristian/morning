import datetime
import requests
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import random
import datetime

def morning_update_dates():
    today = datetime.datetime.now()
    today_formatted = today.strftime("%A, %B %d, %Y")
    new_years_day = datetime.datetime(today.year + 1, 1, 1)
    birthday = datetime.datetime(today.year, 2, 5)
    lindsay_birthday = datetime.datetime(today.year, 6, 6)
    if today > birthday:
        birthday = datetime.datetime(today.year + 1, 2, 5)
    if today > lindsay_birthday:
        lindsay_birthday = datetime.datetime(today.year + 1, 6, 6)
    days_until_new_years = (new_years_day - today).days
    days_until_birthday = (birthday - today).days
    days_until_lindsay_birthday = (lindsay_birthday - today).days
    return today_formatted, days_until_new_years, days_until_birthday, days_until_lindsay_birthday