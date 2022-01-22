import json
import requests

city_name = str(input("Введите имя города:"))
API_key = '6440b74da23867d7cabf14b30f57a6bd'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'

res = requests.get(API_url)
# print(res)

json_data = res.json()
print("Температура:",json_data['main']['temp'])
print("Ощушается как:",json_data['main']['feels_like'])
dic = {"Clouds":"Облачно","Clear":"Чисто","Rain":"Дождь","Snow":"Снег","Wind":"Ветренно"}
st = json_data['weather'][0]['main']
if st in dic:
    print("Состояние:",dic[st])
else:
    print("Статус:", st)





