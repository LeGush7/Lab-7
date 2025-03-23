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
    data_dict = requests.get(url_dict).json()
    if not data_dict or not isinstance(data_dict, list) or \
            len(data_dict) == 0:
        print('Такого слова нет в словаре')
        sys.exit()

    first_entry = data_dict[0]

    if 'meta' in first_entry and 'stems' in first_entry['meta']:
        print(f"Схожие слова или выражения: "
              f"{', '.join(first_entry['meta']['stems'])}")
    else:
        print("Схожие слова или выражения: информация отсутствует")

    if 'hwi' in first_entry and 'prs' in first_entry['hwi']\
            and len(first_entry['hwi']['prs']) > 0:
        pronunciation = first_entry['hwi']['prs'][0].get('mw',
                                                         'информация отсутствует')
        print(f"Транскрипция в формате Merriam-Webster: {pronunciation}")

        if 'sound' in first_entry['hwi']['prs'][0] and \
                'audio' in first_entry['hwi']['prs'][0]['sound']:
            audio_url = f'https://media.merriam-webster.com/' \
                        f'audio/prons/en/us/mp3/{word[0]}/' \
                        f'{first_entry["hwi"]["prs"][0]["sound"]["audio"]}.mp3'
            webbrowser.open_new(audio_url)
            print("Произношение: (отдельное окно в браузере)")
        else:
            print("Произношение: аудио отсутствует")
    else:
        print("Транскрипция и произношение: информация отсутствует")

    if 'shortdef' in first_entry and len(first_entry['shortdef']) > 0:
        shortdef = re.sub(r'{.*?}', '', first_entry['shortdef'][0])
        print(f"Краткое определение: {shortdef}")
    else:
        print("Краткое определение: информация отсутствует")

    if 'et' in first_entry and len(first_entry['et']) > 0:
        etymology = re.sub(r'{.*?}', '', first_entry['et'][0][1])
        print(f"Этимология: {etymology}")
    else:
        print("Этимология: информация отсутствует")

except Exception as e:
    print(f"Произошла ошибка при обработке слова: {e}")

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
        pict = pict.resize((new_width, new_height), Image.Resampling.LANCZOS)
        pict = ImageTk.PhotoImage(pict)
        show_pict.image_label = Label(root, image=pict)
        show_pict.image_label.image = pict
        show_pict.image_label.pack()


root = Tk()
root.title('Изображение дня')
btn = Button(root, text='Загрузить изображение', command=show_pict)
btn.pack(pady=20)
root.mainloop()
