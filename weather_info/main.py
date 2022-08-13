import requests # this is a library for sending requests to any website
from pprint import pprint

API_Key = '85c931d9de25ba4772e49c494b0ee458'

city = input("Enter a city: ")

base_url = "https://openweathermap.org/data/2.0/weather?appid=" + API_Key + "&q" + city

weather_data = requests.get(base_url).json()

pprint(weather_data)
