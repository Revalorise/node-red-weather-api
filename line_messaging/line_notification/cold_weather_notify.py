import os
import requests
from modules import get_temp, get_time
from dotenv import load_dotenv


load_dotenv()

url = "https://notify-api.line.me/api/notify"
token = os.getenv("LINE_NOTIFY_TOKEN")

headers = {'content-type': 'application/x-www-form-urlencoded',
           'Authorization': 'Bearer ' + token}

img = 'https://miro.medium.com/v2/resize:fit:860/1*S4WIvQNuinYTX2111NyXAg.jpeg'
temp = get_temp()
current_time = get_time()

response = {'message': f"It's getting cold outside, the current temperature is {temp}°C as of [{current_time}]",
            'imageThumbnail': img, 'imageFullsize': img}

session = requests.Session()
session.post(url, headers=headers, data=response)
