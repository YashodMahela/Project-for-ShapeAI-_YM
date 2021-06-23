import requests
#import os
from datetime import datetime



api_key = '7ca1519281bf23ee1506e46bb507b4b8'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

#write data to a weather file usin append

file = open("weather.txt","w")

hr          = "\n-------------------------------------------------------------\n"
city_name   = "\nWeather Stats for - {}  || {}".format(location.upper(), date_time)
temp        = "\nCurrent temperature is: {:.2f} deg C".format(temp_city)
weath       = "\nCurrent weather desc  :"+str(weather_desc)
hm          = "\nCurrent Humidity      :"+str(hmdt)+ '%' 
wind        = "\nCurrent wind speed    :"+str(wind_spd) +'kmph'
file.write(hr)
file.write(city_name)
file.write(hr)
file.write(temp)
file.write(weath)
file.write(hm)
file.write(wind)

file.close()
