import csv
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import json

cities = [
    {'name': 'Seoul', 'latitude': 37.56, 'longitude': 126.97},
    {'name': 'London', 'latitude': 51.50, 'longitude': -0.12},
    {'name': 'New York', 'latitude': 40.71, 'longitude': -74.00}
]

def get_weather(latitude, longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto'

    response = requests.get(url)
    json_data = json.loads(response.text)
    print(f"{json_data['current_weather']['temperature']}도")

for city in cities:
    print(f"{city['name']}의 날씨")
    get_weather(city['latitude'], city['longitude'])