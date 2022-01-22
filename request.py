from urllib import request
import requests

# url = "https://oc.kg/"

# res = requests.get (url)

# print(res)
# print("Статус кода",res.status_code)
# print("Контент сайта",res.content)
# print(res.headers)
# print("URL сайта",res.url)
# print("Ссылки из сайта",res.links)
# print("Тип кодировки",res.encoding)
# print("Тип запроса",res.request.method)



"""open"""
#r
#w
#a
#x

#создать файл
# my_file = open("my_file.txt","x")

#записать файл
# my_file2= open("my_file.txt", "w")
# my_file2.write("Hello world!!!\n")
# my_file2.close()

#Добавить запись в конце
# my_file3 = open("my_file.txt", "a")
# my_file3.write("Hello everybody")
# my_file3.close

# import requests
# url = "https://oc.kg/"
# res = requests.get(url) 
# print(res)   # код статуса
# print(res.content)      
# print(res.headers)
# print("Статуса кода:",res.status_code)
# print("Тип запроса:",res.request)
# print("Тип запроса:",res.request.method)
# print("URL сайта:",res.url)
# print("Тип кодировки(юникод)",res.encoding)
# print("Контент сайта",res.content)
# print(res.links)
# print(type(res.links))my_file = open("my_file.txt","x")
# ", "x")
# записать в файл
# my_file2 = open("new_file.txt", "a")
# my_file2.write("Hello world!!!\n")
# my_file2.close()
# добавить запись в конце
# my_file3 = open("new_file.txt", "w")
# my_file3.write("H..........\n")
# my_file3.close()
# my_file4 = open("new_file.txt", "a+")
# my_file4.write("Python\n")
# print(my_file4.read())
# my_file4.close()
# my_file6 = open("new_file.txt", 'a+')      # для записи и чтения  
# my_file6.write("New words")
# my_file6.read()
# my_file6.close()
# my_file5 = open("new_file.txt", "r")
# print(my_file5.read())
# for i in my_file5:
#     print(i, "good")
# m = my_file5.readlines()
# print(m)
# print(type(m))
# c = 0
# y = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "h":
#             c += 1
#         elif letter.lower() == "y":
#             y += 1
# print("h:",c)
# print("y:", y)
# создать файл
# my_file = open("my_file.txt", "x")
# # Исключение
# file_name = input("Напишите название для создания файла: ")
# try:
#     new = open(file_name, "x")
#     print("Файл создан")
# except FileExistsError:
#     print("Такой файл уже существует!!!")
# o = open("new_file.txt", "w", encoding="UTF-8")
# o.write("Всем привет!   !!  \n")
# o.write("Всем привет!!!")
# o.close()
# o2 = open("new_file.txt", "r")
# print(o2.read())
# print(o2.readlines())     # list
# print(o2.readline())      # str
# print(o2.read(4))
# import os
# os.remove("s")            # remove file
# os.rmdir("nnnnnnnnnn")    # remove directory
# os.mkdir("myy")             # создать папку
# file = input("file name")
# text = input("text")
# # 4
# g = open(file, "w")
# g.write(text)
# inp2 = input("Как хотите назвать файл:")
# inp = input("Вставьте url сайта:")
# if 'www' in inp:
#     inp3 = inp.split(".")
#     inp2 = inp3[1]
#     # print(inp2)
#     res = requests.get (inp)
#     print(res.status_code)
#     if res.status_code==200:
#         my_file = open(f"{inp2}.html","x")
#         my_file2= open(f"{inp2}.html", "w")
#         my_file2.write(f"{res.text}")
#     else:
#         print("Вставлена неправильная ссылка!")
# else:
#     inp4 = inp.split("/")
#     inp5 = inp4[2]
#     print(inp5)
#     res = requests.get (inp)
#     if res.status_code==200:
#         my_file = open(f"{inp5}.html","x")
#         my_file2= open(f"{inp5}.html", "w")
#         my_file2.write(f"{res.text}")
#     else:
#         print("Вставлена неправильная ссылка!")
# with open('oc.kg.html') as f:
#     print(sum(1 for _ in f))



























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
