import os
import requests
from modules import get_temp, get_time
from dotenv import load_dotenv


load_dotenv()

url = "https://notify-api.line.me/api/notify"
token = os.getenv("LINE_NOTIFY_TOKEN")

headers = {'content-type': 'application/x-www-form-urlencoded',
           'Authorization': 'Bearer ' + token}

img_url = 'https://www.wkrn.com/wp-content/uploads/sites/73/2021/07/GettyImages-1150050227.jpg?w=774'
temp = get_temp()
current_time = get_time()

response = {'message': f"It's getting hot outside, the current temperature is {temp}°C as of [{current_time}]",
            'imageThumbnail': img_url, 'imageFullsize': img_url}

session = requests.Session()
session.post(url, headers=headers, data=response)