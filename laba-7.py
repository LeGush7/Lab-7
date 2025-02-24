import requests
import json

# первое задание
api_key_weather = '6a44263814d48cbe2101ccda16e0f365'
city_name = 'Kutná Hora'
url_weather = f'https://api.openweathermap.org/data/2.5/weather?' \
              f'q={city_name}&lang=ru&appid={api_key_weather}&units=metric'
data_weather = requests.get(url_weather).json()
print(f"""Город: {city_name}
Погода: {data_weather['weather'][0]['description']}
Давление: {data_weather['main']['pressure']} мм рт. ст.
Влажность: {data_weather['main']['humidity']}%""")


