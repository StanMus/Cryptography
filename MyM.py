# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import *
import random

def fu(a):
    return a*2

change=1

def get_coding(letter, max_rnd, lst):
    rnd_index = random.randint(0, max_rnd)
    rez = -1
    for i in range(rnd_index, len(lst)):
        if lst[i] == letter:
            rez = i
            break
    return rez

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

def coding_click(event):
    lst = get_lst()
    max_rnd = round(len(lst[0]) - 0.3*len(lst[0]))
    coding = []
    for i in range(len(lst[1])):
        txt2 = get_coding(lst[1][i], max_rnd, lst[0])
        coding.append(txt2)
    coding = coding[0:len(coding) - 1]
    flag = 0
    for i in range(len(coding)):
        if coding[i] == -1:
            flag = 1
    if flag == 1:
        output.delete('1.0', 'end')
        output.insert("0.0", 'Словарь не подходит для кодирования.')
    else:
        output.delete('1.0', 'end')
        output.insert("0.0", coding)

def get_decoding(num):
    lst = get_lst()
    rez = lst[0][num]
    return rez

def decoding_click(event):
    decod_txt = txt2cod.get('1.0', 'end')
    decod_txt_str = []
    for i in range(len(decod_txt)):
        decod_txt_str.append(str(decod_txt[i]))
    decod_txt_str = decod_txt_str[0:len(decod_txt_str)-1]
    decod_txt_str.append(str(' '))
    decod_txt_int = []
    count = ''
    for i in range(len(decod_txt_str)):
        if decod_txt_str[i] != ' ':
            count = count + decod_txt_str[i]
        else:
            count_int = int(count)
            decod_txt_int.append(count_int)
            count = ''
            count_int = 0
    print(decod_txt_int)
    lst = get_lst()
    decoding = []
    for i in range(len(decod_txt_int)):
        txt2 = get_decoding(decod_txt_int[i])
        decoding.append(txt2)
    decoding = ''.join(decoding)
    output.delete('1.0', 'end')
    output.insert("0.0", decoding)

def clear(event):
    output.delete('1.0', 'end')
    txt2cod.delete('1.0', 'end')

def save(event):
    file = open('results.txt', 'w')
    file.write(output.get('0.0', 'end'))
    file.close()

window = Tk()
window.title("Шифратор и дешифратор на основе алгоритма «Блокнот»")
window.iconbitmap(u'main.ico')
window.resizable(width=False, height=False)
window.configure(bg='white')
frame1 = Frame(window, width=780, height=410)
frame1.grid(row=0, column=0)
label1 = Label(frame1, text='Исходный текст:', width=40, font="Verdana 11")
label1.place(x=10, y=10)
txt2cod = Text(frame1, width=36, height=15, bd=2, font="Verdana 11", wrap=WORD)
txt2cod.config(state=NORMAL)
txt2cod.place(x=10, y=35)
label2 = Label(frame1, text='Результат:', width=40, font="Verdana 11")
label2.place(x=400, y=10)
output = Text(frame1, bg="white", font="Verdana 11", width=36, height=15, bd=2, wrap=WORD)
output.config(state=NORMAL)
output.place(x=400, y=35)
label3 = Label(frame1, text='Файл со словарем:', width=20, font="Verdana 11")
label3.place(x=10, y=315)
libEntry = Entry(frame1, width=18, bd=2, font="Verdana 11")
libEntry.insert(END, 'dictionary.txt')
libEntry.place(x=10, y=340)
btnCod = Button(frame1, width=14, bg='white', font="Verdana 11")
btnCod.place(x=430, y=330)
btnCod['text'] = 'Кодировать'
btnCod.bind('<Button-1>', coding_click)
btnDec = Button(frame1, width=14, bg='white', font="Verdana 11")
btnDec.place(x=590, y=330)
btnDec['text'] = 'Декодировать'
btnDec.bind('<Button-1>', decoding_click)
btnClear = Button(frame1, width=14, bg='white', font="Verdana 11")
btnClear.place(x=220, y=330)
btnClear['text'] = 'Очистить'
btnClear.bind('<Button-1>', clear)
btnSave = Button(frame1, width=14, bg='white', font="Verdana 11")
btnSave.place(x=220, y=370)
btnSave['text'] = 'Сохранить'
btnSave.bind('<Button-1>', save)
window.mainloop()
