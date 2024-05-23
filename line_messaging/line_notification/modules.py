import json
from datetime import datetime


def get_temp():
    with open('../../dashboard/src/data/current_Thai_weather_transformed.json', 'r') as f:
        data = json.load(f)
        return data['main']['temp']


def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    return current_time