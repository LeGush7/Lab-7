import requests
import webbrowser
import re
import sys
from tkinter import Tk, Button, Label
from PIL import Image, ImageTk
from io import BytesIO

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
Этимология: {re.sub(r'{.*?}', '', data_dict['et'][0][1])}""")

# доп задание
api_nasa = 'z2QfXds3G5wxMPAGXoikUVxh4zqg7b8DWdhhUSoH'
url_nasa = f'https://api.nasa.gov/planetary/apod?api_key={api_nasa}'
data_nasa = requests.get(url_nasa).json()
image_nasa = data_nasa['hdurl']


def show_pict():
        pict = Image.open(BytesIO(requests.get(image_nasa).content))
        width, height = pict.size
        new_width = 720
        new_height = int(height * (new_width / width))
        pict = pict.resize((new_width, new_height),
                             Image.Resampling.LANCZOS)
        pict = ImageTk.PhotoImage(pict)
        show_pict.image_label = Label(root, image=pict)
        show_pict.image_label.image = pict
        show_pict.image_label.pack()


root = Tk()
root.title('Изображение дня')
btn = Button(root, text='Загрузить изображение', command=show_pict)
btn.pack(pady=20)
root.mainloop()
