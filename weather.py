# get the weather according to the api at open-weather-map

import json, requests

ZIPCODE = '97205'
with open('./.api_keys.json', 'r') as f:
    keys = json.loads(f.read())
    API_KEY = keys.get('open-weather')

def get_weather():
    res = requests.get(f'http://api.openweathermap.org/data/2.5/weather?zip={ZIPCODE},us&appid={API_KEY}&units=imperial')
    weather = json.loads(res.content)
    cur_weather = weather.get('main')
    return cur_weather