import requests
import webbrowser
import re
import sys

# # первое задание
api_key_weather = '6a44263814d48cbe2101ccda16e0f365'
city_name = 'Kutná Hora'
url_weather = f'https://api.openweathermap.org/data/2.5/weather?' \
              f'q={city_name}&lang=ru&appid={api_key_weather}&units=metric'
data_weather = requests.get(url_weather).json()
print(f"""Город: {city_name}
Погода: {data_weather['weather'][0]['description']}
Давление: {data_weather['main']['pressure']} мм рт. ст.
Влажность: {data_weather['main']['humidity']}%""")
print()


# второе задание
api_key_dict = 'da63a6ce-28db-43e3-adbf-3efe89efb2e2'
word = str(input('Введите слово на английском: '))
url_dict = f'https://www.dictionaryapi.com/api/v3/' \
           f'references/collegiate/json/{word}?key={api_key_dict}'
try:
    data_dict = requests.get(url_dict).json()[0]
except Exception:
    print('Такого слова нет в словаре')
    sys.exit()
print(f"""Схожие слова или выражения: {', '.join(data_dict['meta']['stems'])}
Транскрипция в формате Merriam-Webster: {data_dict['hwi']['prs'][0]['mw']}
Произношение: (отдельное окно в браузере)""")
webbrowser.open_new(f'https://media.merriam-webster.com/'
                    f'audio/prons/en/us/mp3/{word[0]}/'
                    f'{data_dict["hwi"]["prs"][0]["sound"]["audio"]}.mp3')
print(f"""Краткое определение: {re.sub(r'{.*?}', '', data_dict["shortdef"][0])}
Этимология: {re.sub(r'{.*?}', '', data_dict["et"][0][1])}""")
