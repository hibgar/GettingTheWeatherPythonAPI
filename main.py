# Get the current weather for a given zip/postal code. Optional: Try locating the user automatically.
# API doc: https://openweathermap.org/api/one-call-api

import json
import requests

response_API = requests.get(
    'https://api.openweathermap.org/data/2.5/onecall?lat=[LAT]&lon=[LON]&exclude=current,hourly,minutely&units=imperial&appid=[API KEY]'
)

forecast = response_API.json()['daily'][0]
today_weather = forecast['weather'][0]['description']

tempto = response_API.json()['daily'][0]
today = tempto['temp']['day']
print("The temperature today is", today)

temptmrw = response_API.json()['daily'][1]
tmrw = temptmrw['temp']['day']
print("The temperature tomorrow is", tmrw)

if 'rain' in today_weather:
  print('It\'s going to rain today \U00002614, take your umbrella with you!')
else:
  print('Hooray! You won\'t need your umbrella today!')