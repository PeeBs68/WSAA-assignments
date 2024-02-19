# currentweather.py

# Author: Phelim Barry

# Purpose: outputs the current temperature (2m) and current wind direction (10m) to the console

# Using latitude = 51.734507 & longitude = -8.539811 (Kinsale Golf Club, Co. Cork!)

import json
import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=51.734507&longitude=-8.539811&current=temperature_2m&current=wind_direction_10m"

response = requests.get(url)
data = response.json()

current_wdir = data["current"]["wind_direction_10m"]
current_temp = data["current"]["temperature_2m"]

# Just to add a bit more detail
# wind directions from : https://uni.edu/storm/Wind%20Direction%20slide.pdf
if current_wdir < 90:
    wdir = "North/Easterly"
elif current_wdir < 180:
    wdir = "South/Easterly"
elif current_wdir < 279:
    wdir = "West/Southerly"
else:
    wdir = "North/Westerly"

print(f"Right now at Kinsale Golf Club the temperature is {current_temp} degrees celcius and the wind direction is {current_wdir} degrees (which means it is roughly {wdir})")
