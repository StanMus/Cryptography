# -*- coding: utf-8 -*-
from tkinter import *

def get_lst():
    txt = txt2cod.get('1.0', 'end')
    cod_txt = []
    for i in txt:
        cod_txt.append(str(i))
    k = libEntry.get()
    file = open(libEntry.get(), 'r', encoding="utf8")
    line = file.read()
    lst = []
    for i in line:
        lst.append(str(i))
    return lst, cod_txt

window = Tk()
window.title("Шифратор и дешифратор на основе алгоритма «Блокнот»")
window.iconbitmap(u'main.ico')
window.resizable(width=False, height=False)
window.configure(bg='white')
frame1 = Frame(window, width=780, height=410)
frame1.grid(row=0, column=0)
label1 = Label(frame1, text='Исходный текст:', width=40, font="Verdana 11")
label1.place(x=10, y=10)
txt2cod = Text(frame1, width=36, height=15, bg='grey', bd=2, font="Verdana 11", wrap=WORD)
txt2cod.config(state=NORMAL)
txt2cod.place(x=10, y=35)

window.mainloop()
