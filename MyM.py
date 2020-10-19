# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import *
import random

коды

def get_coding(letter, max_rnd, lst):
    rnd_index = random.randint(0, max_rnd)
    rez = -1
    for i in range(rnd_index, len(lst)):
        if lst[i] == letter:
            rez = i
            break
    return rez

def get_lst():
    txt = txt2cod.get('1.0', 'end-1c')
    cod_txt = []
    for i in txt:
        cod_txt.append(str(i))
    return cod_txt

def get_gamma(txt):
    gamma = []
    for i in range(0, len(txt)*8):
        rand_num = random.randint(0, 1)
        gamma.append(str(rand_num))
    gamma_digital = ''.join(gamma)

    # Сохранить gamma в отдельный файл
    file = open('gamma.txt', 'w')
    file.write(gamma_digital)

    return gamma_digital

def my_test(event):
    var1 = get_lst()
    var2 = get_gamma(var1)
    var4 = lst_digital(var1)
    var3 = load_dict()
    # a = var.cod_txt
    # b = var.lst
    # a = [var, type(var)]
    output.insert('0.0', var2)

def load_dict():
    file = open(libEntry.get(), 'r', encoding="utf8")
    dict_str = file.read()
    dict_list = dict_str.split('\n')
    key_list = []
    value_list = []
    for i in dict_list:
        i_list = i.split(' = ')
        key = i_list[0]
        value = i_list[1]
        key_list.append(str(key))
        value_list.append(str(value))
    dict_digital = {}
    dict_letters = {}
    for j in range(0, len(key_list)):
        dict_digital[key_list[j]] = value_list[j]
    for k in range(0, len(key_list)):
        dict_letters[value_list[k]] = key_list[k]
    return dict_digital, dict_letters

def lst_digital(lst): # перевод исходного текста в двоичный код
    dict_digital = load_dict()[0]
    lst_digital = []
    try:
        for i in lst:
            element = dict_digital['{}'.format(i)]
            lst_digital.append(element)
        lst_digital = ''.join(lst_digital)
    except KeyError:
        lst_digital = []
    return lst_digital

def make_code(lst_dig, gamma_dig):
    lst_digital = []
    for i in lst_dig:
        lst_digital.append(int(i))

    gamma_digital = []
    for i in gamma_dig:
        gamma_digital.append(int(i))

    code = []
    for i in range(0, len(lst_digital)):
        text = int(lst_digital[i])
        gamma = int(gamma_digital[i])
        if text==1 and gamma==1:
            code.append(0)
        elif text==0 and gamma==1:
            code.append(1)
        elif text==1 and gamma==0:
            code.append(1)
        elif text==0 and gamma==0:
            code.append(0)
    code_digital = ''.join(str(i) for i in code)
    return code_digital

def make_letters(code_digital):
    dict_letters = load_dict()[1]
    code_di = []
    for i in code_digital:
        code_di.append(int(i))
    n_letters = int(len(code_di) / 8) # сделать ветку, что может быть нецелый результат
    code_le = []
    for i in range(0, n_letters):
        letter_di = code_di[i*8 : (i+1)*8]
        letter = ''.join(str(j) for j in letter_di)
        code_le.append(letter)
    code_letters = []
    try:
        for i in code_le:
            element = dict_letters['{}'.format(i)]
            code_letters.append(element)
        code_letters = ''.join(code_letters)
    except KeyError:
        code_letters = []
    return code_letters

def coding_click(event):
    lst = get_lst()
    lst_dig = lst_digital(lst)
    if lst_dig == []:
        output.delete('1.0', 'end')
        output.insert('0.0', 'Невозможно зашифровать символ исходного текста')
    else:
        gamma_digital = get_gamma(lst)
        code_digital = make_code(lst_dig, gamma_digital)
        code_letters = make_letters(code_digital)
        output.delete('1.0', 'end')
        output.insert("0.0", code_letters)

def get_decoding(num):
    lst = get_lst()
    rez = lst[0][num]
    return rez

def decoding_click(event):
    code_letters = output.get('1.0', 'end-1c')
    txt2cod.delete('1.0', 'end')
    txt2cod.insert('0.0', code_letters)

    lst = get_lst()
    lst_dig = lst_digital(lst)
    if lst_dig == []:
        output.delete('1.0', 'end')
        output.insert('0.0', 'Невозможно зашифровать символ исходного текста')
    else:
        gamma_file = 'gamma.txt'
        file = open(gamma_file, 'r', encoding="utf8")
        gamma_digital = file.read()

        code_digital = make_code(lst_dig, gamma_digital)
        code_letters = make_letters(code_digital)
        output.delete('1.0', 'end')
        output.insert("0.0", code_letters)

def clear(event):
    output.delete('1.0', 'end')
    txt2cod.delete('1.0', 'end')

def save_text(event):
    file = open('results.txt', 'w')
    file.write(output.get('0.0', 'end'))
    file.close()

def load_text(event):
    a=1

def open_dictionary(event):
    a=1

def open_gamma(event):
    a=1


window = Tk()
window.title("Шифратор и дешифратор на основе алгоритма «Блокнот»")
window.iconbitmap(u'main.ico')
window.resizable(width=False, height=False)
window.configure()
frame1 = Frame(window, width=780, height=410, bg='#E7E6E6')
frame1.grid(row=0, column=0)
label1 = Label(frame1, text='Исходный текст:', bg='#E7E6E6', font="Verdana 11")
label1.place(x=30, y=10, width=340)
txt2cod = Text(frame1, bg='white', font="Verdana 11", wrap=WORD)
txt2cod.config(state=NORMAL)
txt2cod.place(x=30, y=35, width=340, height=220)
label2 = Label(frame1, text='Результат:', bg='#E7E6E6', font="Verdana 11")
label2.place(x=410, y=10, width=340)
output = Text(frame1, bg="white", font="Verdana 11", wrap=WORD)
output.config(state=NORMAL)
output.place(x=410, y=35, width=340, height=220)

btnLoad = Button(frame1, bg='white', bd=0, font="Verdana 11")
btnLoad.place(x=30, y=263, width=150, height=20)
btnLoad['text'] = 'Загрузить текст'
btnLoad.bind('<Button-1>', load_text)

btnSave = Button(frame1, bg='white', bd=0, font="Verdana 11")
btnSave.place(x=600, y=263, width=150, height=20)
btnSave['text'] = 'Сохранить результат'
btnSave.bind('<Button-1>', save_text)

label3 = Label(frame1, text='Словарь:', bg='#E7E6E6', font="Verdana 11")
label3.place(x=30, y=335, width=70, height=25)
libEntry = Entry(frame1, bg="white", bd=0, font="Verdana 11")
libEntry.insert(END, 'dictionary.txt')
libEntry.place(x=120, y=335, width=120, height=25)
btnOpenD = Button(frame1, bg='white', bd=0, font="Verdana 11")
btnOpenD.place(x=260, y=335, width=110, height=25)
btnOpenD['text'] = 'Открыть'
btnOpenD.bind('<Button-1>', open_dictionary)

label4 = Label(frame1, text='Гамма:', bg='#E7E6E6', font="Verdana 11")
label4.place(x=30, y=365, width=60, height=25)
libEntry2 = Entry(frame1, bg="white", bd=0, font="Verdana 11")
libEntry2.insert(END, 'gamma.txt')
libEntry2.place(x=120, y=365, width=120, height=25)
btnOpenG = Button(frame1, bg='white', bd=0, font="Verdana 11")
btnOpenG.place(x=260, y=365, width=110, height=25)
btnOpenG['text'] = 'Открыть'
btnOpenG.bind('<Button-1>', open_gamma)

btnCod = Button(frame1, bg='white', bd=0, font="Verdana 11")
btnCod.place(x=260, y=263, width=110, height=25)
btnCod['text'] = 'Кодировать'
btnCod.bind('<Button-1>', coding_click)
btnDec = Button(frame1, width=14, bg='white', font="Verdana 11")
btnDec.place(x=410, y=263, width=110, height=25)
btnDec['text'] = 'Декодировать'
btnDec.bind('<Button-1>', decoding_click)

btnClear = Button(frame1, bg='white', font="Verdana 11")
btnClear.place(x=650, y=300, width=100)
btnClear['text'] = 'Очистить'
btnClear.bind('<Button-1>', clear)

btnSave = Button(frame1, width=14, bg='white', font="Verdana 11")
btnSave.place(x=220, y=370)
btnSave['text'] = 'Сохранить'
btnSave.bind('<Button-1>', save)

window.mainloop()
