import json


def get_temp():
    with open('../../dashboard/src/data/current_Thai_weather_transformed.json', 'r') as f:
        data = json.load(f)
        return data['main']['temp']
