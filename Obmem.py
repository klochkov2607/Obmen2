from logging import exception
from unittest import expectedFailure

import requests
import json
from tkinter import*
from tkinter import messagebox as mb

from bottle import response


def exchange():
    code=entry.get()

    if code:
        try:
            response=requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()# raise_for_status, если все хорошо
            data=response.json()
            if code in data["rates"]:
                exchange_rate=data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс:{exchange_rate} {code} за 1 доллар")
            else:
                mb.showerror("Ошибка!", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")


window=Tk()# создаем оконный интерфейс
window.title ("Курсы обмена валют")
window.geometry("360x180")
Label(text="Введите код валюты").pack(padx=10, pady=10)# метка безымянная

entry=Entry()# поле ввода Entry
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
