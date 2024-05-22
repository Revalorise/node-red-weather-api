import json
from utils_function.convert_functions import kelvin_to_celsius, convert_epoch_to_timestamp
from pprint import pprint


def transform(data):
    for i in range(len(data['list'])):
        data['list'][i].pop('clouds', None)
        data['list'][i].pop('dt', None)
        data['list'][i].pop('visibility', None)
        data['list'][i].pop('wind', None)

        data['list'][i]['main']['temp'] = kelvin_to_celsius(data['list'][i]['main']['temp'])
        data['list'][i]['main']['feels_like'] = kelvin_to_celsius(data['list'][i]['main']['feels_like'])


if __name__ == "__main__":
    with open("../weather_data/forecast_Thai_weather.json", "r") as f:
        data = json.load(f)

    transform(data)

    with open("../dashboard/src/data/forecast_Thai_weather_transformed.json", "w") as f:
        json.dump(data, f, indent=4)
