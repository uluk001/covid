

import json 
import requests
from googletrans import Translator



translator = Translator()
cc= int(input("""
1-Country
2-City:"""))
lang = int(input("""Choose language:
1-English
2-Русский
3-Кыргызча:"""))
if cc==1:
    if lang==1:
        t = translator.translate("Название страны:", dest='en').text
        country = input(t)
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        q = 'Название страны:'
        w = 'Потверждено:'
        e = 'Выздоровели:'
        r = 'Умерли:'
        json_covid = res.json()
        print(translator.translate(q, dest='en').text, json_covid['All']['country'])
        print(translator.translate(w, dest='en').text, json_covid['All']['confirmed'])
        print(translator.translate(e, dest='en').text, json_covid['All']['recovered'])
        print(translator.translate(r, dest='en').text, json_covid['All']['deaths'])
    elif lang==2:
        t = translator.translate("Название страны:", dest='ru').text
        country = input(t)
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        q = 'Название страны:'
        w = 'Потверждено:'
        e = 'Выздоровели:'
        r = 'Умерли:'
        json_covid = res.json()
        print(translator.translate(q, dest='ru').text, json_covid['All']['country'])
        print(translator.translate(w, dest='ru').text, json_covid['All']['confirmed'])
        print(translator.translate(e, dest='ru').text, json_covid['All']['recovered'])
        print(translator.translate(r, dest='ru').text, json_covid['All']['deaths'])
    elif lang==3:
        t = translator.translate("Название страны:", dest='ky').text
        country = input(t)
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        q = 'Название страны:'
        w = 'Потверждено:'
        e = 'Выздоровели:'
        r = 'Умерли:'
        json_covid = res.json()
        print(translator.translate(q, dest='ky').text, json_covid['All']['country'])
        print(translator.translate(w, dest='ky').text, json_covid['All']['confirmed'])
        print(translator.translate(e, dest='ky').text, json_covid['All']['recovered'])
        print(translator.translate(r, dest='ky').text, json_covid['All']['deaths'])
    else:
        print("Неверная операция")
elif cc==2:
    if lang==1:
        t = translator.translate("Название страны:", dest='en').text
        cccc = translator.translate("Название города:", dest='en').text
        country = input(t)
        ccc = input(cccc).title()
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        q = 'Название страны:'
        w = 'Потверждено:'
        e = 'Выздоровели:'
        r = 'Умерли:'
        json_covid = res.json()
        try:
            print(translator.translate(w, dest='ru').text, json_covid[f'{ccc}']['confirmed'])
            print(translator.translate(e, dest='ru').text, json_covid[f'{ccc}']['recovered'])
            print(translator.translate(r, dest='ru').text, json_covid[f'{ccc}']['deaths'])
        except KeyError:
            print("Нету такого города!!!")
    elif lang==2:
        t = translator.translate("Название страны:", dest='ru').text
        cccc = translator.translate("Название города:", dest='ru').text
        country = input(t).title()
        ccc = input(cccc).title()
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        q = 'Название страны:'
        w = 'Потверждено:'
        e = 'Выздоровели:'
        r = 'Умерли:'
        json_covid = res.json()
        # print(translator.translate(q, dest='ru').text, json_covid[f'{ccc}']['country'])
        try:
            print(translator.translate(w, dest='ru').text, json_covid[f'{ccc}']['confirmed'])
            print(translator.translate(e, dest='ru').text, json_covid[f'{ccc}']['recovered'])
            print(translator.translate(r, dest='ru').text, json_covid[f'{ccc}']['deaths'])
        except KeyError:
            print("Нету информации об этом городе!!!")
    elif lang==3:
        t = translator.translate("Название страны:", dest='ky').text
        cccc = translator.translate("Название города:", dest='ky').text
        country = input(t).title()
        ccc = input(cccc).title()
        url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
        res  = requests.get(url)
        q = 'Название страны:'
        w = 'Потверждено:'
        e = 'Выздоровели:'
        r = 'Умерли:'
        json_covid = res.json()
        try:
            print(translator.translate(w, dest='ky').text, json_covid[f'{ccc}']['confirmed'])
            print(translator.translate(e, dest='ky').text, json_covid[f'{ccc}']['recovered'])
            print(translator.translate(r, dest='ky').text, json_covid[f'{ccc}']['deaths'])
        except KeyError:
            print("Тилекке каршы бул шаар жонундо маалымат жок!!!")
    else:
        print("Неверная операция")
else:
    print("Неверная операция")
