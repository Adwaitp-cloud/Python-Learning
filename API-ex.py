import pandas as pd

import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

type(data)
data.keys()
data["current"]["time"]
data["current"]["temperature_2m"]


import requests

def get_weather(latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.68, 139.69)
nagpur_temp = get_weather(21.1458, 79.0882)
boisar_temp = get_weather(19.7969, 72.7452)


print(f"Paris: {paris_temp}°C")
print(f"London: {london_temp}°C")
print(f"Tokyo: {tokyo_temp}°C")
print(f"Nagpur:{nagpur_temp}°C")
print(f"Boisar:{boisar_temp}°C")

df = pd.read_csv('data/paris_weather.csv')
print(df)

df = pd.read_excel('../Python-Projects/sales-analysis/output/sales_data.xlsx')
print(df)

df = pd.read_json('../Python-Projects/sales-analysis/output/sales_data.json')
print(df)

df = pd.read_csv('../Python-Projects/sales-analysis/output/sales_with_totals.csv')
print(df)

df = open('hello.txt', 'r')
print(df.read())