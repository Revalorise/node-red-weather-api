import json
from utils_function.convert_functions import kelvin_to_celsius, convert_epoch_to_timestamp


def transform(data):
    data['dt'] = convert_epoch_to_timestamp(data['dt'])
    data['main'] = {
        'temp': kelvin_to_celsius(data['main']['temp']),
        'feels_like': kelvin_to_celsius(data['main']['feels_like']),
        'temp_min': kelvin_to_celsius(data['main']['temp_min']),
        'temp_max': kelvin_to_celsius(data['main']['temp_max']),
    }
    data['sys'] = {
        'sunrise': convert_epoch_to_timestamp(data['sys']['sunrise']),
        'sunset': convert_epoch_to_timestamp(data['sys']['sunset']),
    }


if __name__ == "__main__":
    with open("../weather_data/current_Thai_weather.json", "r") as f:
        data = json.load(f)

    transform(data)

    with open("../dashboard/src/data/current_Thai_weather_transformed.json", "w") as f:
        json.dump(data, f, indent=4)
