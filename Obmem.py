'''import requests
import json
import pprint

result=requests.get("https://open.er-api.com/v6/latest/USD")
data=json.loads(result.text)
p=pprint.PrettyPrinter(indent=4)# indent, количество отступов

p.pprint(data)'''

import requests
import json
from tkinter import*
from tkinter import messagebox as mb

# import pprint# функция pprint является основной функцией модуля и позволяет красиво выводить данные на экран

# result=requests.get("https://open.er-api.com/v6/latest/USD")
# data=json.loads(result.text)
# p=pprint.PrettyPrinter(indent=4)# indent, количество отступов

# p.pprint(data)

window=Tk()# создаем оконный интерфейс
window.title ("Курсы обмена валют")
window.geometry("360x180")
Label(text="Введите код валюты").pack(padx=10, pady=10)# метка безымянная

entry=Entry()# поле ввода Entry
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
