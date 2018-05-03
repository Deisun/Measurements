import requests
import json
from datetime import datetime

apiID = '7cca7713d1b5bf4693151f6e60115da9'
zipCode = 30144



# call OpenWeatherAPI to get zip code weather
response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + str(zipCode) + ',us&appid=' + apiID)
# convert response to json format
data = response.json()

# get name
name = data['name']

# get temp
temp = float(data['main']['temp'])
# convert to Farenheit
tempFarenheit = (temp - 273.15) * 1.8 + 32

# get atmospheric pressure
atmosphericPressure = data['main']['pressure']

# get wind speed
windSpeed = data['wind']['speed']

# get wind direction
windDirection = data['wind']['deg']

# get timestamp
timestamp = data['dt']
formattedTime = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


print('Name: ', name)
print('Current Temperature: ', tempFarenheit)
print('Atmospheric Pressure: ', atmosphericPressure)
print('Wind Speed: ', windSpeed)
print('Wind Direction: ', windDirection)
print('Time of Report: ', formattedTime)
