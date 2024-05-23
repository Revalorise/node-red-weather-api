import json
from pprint import pprint


def check_temp(temp):
    if temp <= 25:
        return 0  # 0 = cold
    elif temp > 35:
        return 1  # 1 = hot
    else:
        return 2  # 2 = normal


if __name__ == '__main__':
    with open('../../dashboard/src/data/current_Thai_weather_transformed.json', 'r') as f:
        data = json.load(f)

    temp = check_temp(data['main']['temp'])
    print(temp)
