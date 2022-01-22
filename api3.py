import requests
from googletrans import Translator
import json
inn = int(input("""Выберите язык
1-Enlish
2-Кыргызча
3-Русский
4-中國人
5-French
6-Japanese
7-Italian
8-Bahasa Indonesia
9-                                                                                             عرب
10-한국인:"""))
city_name = str(input("Введите имя города:")).title()
API_key = '6440b74da23867d7cabf14b30f57a6bd'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'
res = requests.get(API_url)
if inn==1:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='en').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='en').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='ky').text
    tt = translator.translate("Погода в", dest='en').text
    print(f"{tt} {city_name}:"  ,a)
elif inn==2:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='ky').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='ky').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='ky').text
    tt = translator.translate("Погода в", dest='ky').text
    print(f"{tt} {city_name}:"  ,a)
elif inn==3:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='ru').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='ru').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='ru').text
    tt = translator.translate("Погода в", dest='ru').text
    print(f"{tt} {city_name}:"  ,a)
elif inn==4:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='zh-tw').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='zh-tw').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='zh-tw').text
    tt = translator.translate("Погода в", dest='zh-tw').text
    print(f"{tt} {city_name}:"  ,a)
elif inn == 5:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='fr').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='fr').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='fr').text
    tt = translator.translate("Погода в", dest='fr').text
    print(f"{tt} {city_name}:"  ,a)
elif inn == 6:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='ja').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='ja').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='ja').text
    tt = translator.translate("Погода в", dest='ja').text
    print(f"{tt} {city_name}:"  ,a)
elif inn == 7:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='it').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='it').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='it').text
    tt = translator.translate("Погода в", dest='it').text
    print(f"{tt} {city_name}:"  ,a)
elif inn == 8:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='id').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='id').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='id').text
    tt = translator.translate("Погода в", dest='id').text
    print(f"{tt} {city_name}:"  ,a)
elif inn == 9:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='ar').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='ar').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='ar').text
    tt = translator.translate("Погода в", dest='ar').text
    print(f"{tt} {city_name}:"  ,a)
elif inn == 10:
    json_data = res.json()
    translator = Translator()
    print(translator.translate("Температура:", dest='ko').text,json_data['main']['temp'])
    print(translator.translate("Ощушается как:", dest='ko').text,json_data['main']['feels_like'])
    st = json_data['weather'][0]['main']
    a = translator.translate(st, dest='ko').text
    tt = translator.translate("Погода в", dest='ko').text
    print(f"{tt} {city_name}:"  ,a)
else:
    print("Неправильная операция")