# get the weather according to the api at open-weather-map

import json, requests

ZIPCODE = '97205'
with open('./.api_keys.json', 'r') as f:
    keys = json.loads(f.read())
    API_KEY = keys.get('open-weather')

def get_weather():
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={0},us&appid={1}&units=imperial'.format(ZIPCODE, API_KEY))
    weather = res.json()
    return weather.get('main')

print(get_weather())