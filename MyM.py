# -*- coding: utf-8 -*-
from tkinter import *
import random
import tkinter.filedialog, tkinter.messagebox
import os
from os import system

def get_lst():
    txt = txt2cod.get('1.0', 'end-1c')
    cod_txt = txt
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
    file.close()

    return gamma_digital

def load_dict(dict_path):
    file = open(dict_path, 'r', encoding="utf8")
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

def lst_digital(lst, dict_digital): # перевод исходного текста в двоичный код
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
    dict_letters = load_dict(dict_path)[1]
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
    dict_digital = load_dict(dict_path)[0]
    lst_dig = lst_digital(lst, dict_digital)
    if lst_dig == []:
        output.delete('1.0', 'end')
        output.insert('0.0', 'Невозможно зашифровать символ исходного текста')
    else:
        gamma_digital = get_gamma(lst)
        code_digital = make_code(lst_dig, gamma_digital)
        code_letters = make_letters(code_digital)
        output.delete('1.0', 'end')
        output.insert("0.0", code_letters)

def decoding_click(event):
    code_letters = output.get('1.0', 'end-1c')
    txt2cod.delete('1.0', 'end')
    txt2cod.insert('0.0', code_letters)

    lst = get_lst()
    dict_digital = load_dict(dict_path)[0]
    lst_dig = lst_digital(lst, dict_digital)
    if lst_dig == []:
        output.delete('1.0', 'end')
        output.insert('0.0', 'Невозможно зашифровать символ исходного текста')
    else:
        gamma_file = 'gamma.txt'
        file = open(gamma_file, 'r', encoding="utf8")
        gamma_digital = file.read()
        file.close()

        code_digital = make_code(lst_dig, gamma_digital)
        code_letters = make_letters(code_digital)
        output.delete('1.0', 'end')
        output.insert("0.0", code_letters)

def clear(event):
    output.delete('1.0', 'end')
    txt2cod.delete('1.0', 'end')

def save_text(event):
    txt = txt2cod.get('1.0', 'end-1c')
    dict_digital = load_dict(dict_path)[0]
    txt_dig = lst_digital(txt, dict_digital)
    txts = 'Исходный текст: ' + txt + ' ({})'.format(txt_dig)

    gamma_file = 'gamma.txt'
    file = open(gamma_file, 'r', encoding="utf8")
    gamma_dig = file.read()
    file.close()
    gamma_letters = make_letters(gamma_dig)
    gammas = 'Гамма: ' + gamma_letters + ' ({})'.format(gamma_dig) + '\n'

    result = output.get('0.0', 'end-1c')
    dict_digital = load_dict(dict_path)[0]
    result_dig = lst_digital(result, dict_digital)
    results = 'Результат: ' + result + ' ({})'.format(result_dig) + '\n'

    file = open('results.txt', 'w')
    file.write(results)
    file.close()

    file = open('results.txt', 'a')
    file.write(gammas)
    file.close()

    file = open('results.txt', 'a')
    file.write(txts)
    file.close()

def load_text(self, filename=None):
    if not filename:
        self.filename = tkinter.filedialog.askopenfilename()
    else:
        self.filename = filename
    if not (self.filename == ''):
        f = open(self.filename, 'r')
        f2 = f.read()
        f.close()
        txt2cod.delete('1.0', 'end')
        txt2cod.insert("0.0", f2)

# Модуль тестирования работоспособности

def test_dialog(event):
    windowT = Tk()
    windowT.title("Тест шифратора")
    windowT.iconbitmap(u'main.ico')
    windowT.resizable(width=False, height=False)
    windowT.configure()
    frameT = Frame(windowT, width=340, height=220, bg='#E7E6E6')
    frameT.grid(row=0, column=0)

    labelT1 = Label(frameT, text='Количество тестов:', bg='#E7E6E6', font="Verdana 11")
    labelT1.place(x=10, y=30, width=150, height=25)
    libEntryT1 = Entry(frameT, bg="white", bd=0, font="Verdana 11")
    libEntryT1.insert(END, 1000)
    libEntryT1.place(x=250, y=30, width=60, height=25)

    labelT2 = Label(frameT, text='Max длина текста:', bg='#E7E6E6', font="Verdana 11")
    labelT2.place(x=10, y=75, width=150, height=25)
    libEntryT2 = Entry(frameT, bg="white", bd=0, font="Verdana 11")
    libEntryT2.insert(END, 15)
    libEntryT2.place(x=250, y=75, width=60, height=25)

    labelT3 = Label(frameT, text='Словарь:', bg='#E7E6E6', font="Verdana 11")
    labelT3.place(x=10, y=120, width=150, height=25)
    libEntryT3 = Entry(frameT, bg="white", bd=0, font="Verdana 11")
    libEntryT3.insert(END, 'dictionary.txt')
    libEntryT3.place(x=190, y=120, width=120, height=25)

    btnTest = Button(frameT, bg='white', bd=0, font="Verdana 11")
    btnTest.place(x=200, y=180, width=110, height=25)
    btnTest['text'] = 'Начать тест'
    btnTest.bind('<Button-1>', testing_click)


    global tests_countG
    global text_lengthG
    global dict_pathG
    tests_countG = int(libEntryT1.get())
    text_lengthG = int(libEntryT2.get())
    dict_pathG = libEntryT3.get()

def testing_click(event):
    global tests_countG
    global text_lengthG
    global dict_pathG

    tests_count = tests_countG
    text_length = text_lengthG
    dict_path = dict_pathG

    # Подготовка словаря
    dict_digital = load_dict(dict_path)[0]
    dict_keys = list(dict_digital)

    for test_number in range(0, tests_count):
        text_len = random.randint(1, text_length)
        text_num = []
        for i in range(0, text_len):
            text_rand_num = random.randint(0, 255)
            text_num.append(text_rand_num)
        text = []
        for i in text_num:
            letter = dict_keys[i]
            text.append(letter)
        text_to_code = ''.join(text)

        # Кодирование
        lst = text_to_code
        lst_dig = lst_digital(lst, dict_digital)
        if lst_dig == []:
            tkinter.messagebox.showinfo('Ошибка', message='Не удалось перевести текст в двоичный код')
        else:
            gamma_digital = get_gamma(lst)
            gamma_letters = make_letters(gamma_digital)
            code_digital = make_code(lst_dig, gamma_digital)
            code_letters = make_letters(code_digital)

        lstSh = code_letters
        lst_digSh = lst_digital(lstSh, dict_digital)
        if lst_digSh == []:
            tkinter.messagebox.showinfo('Ошибка', message='Не удалось перевести шифр в двоичный код')
        else:
            code_digitalSh = make_code(lst_digSh, gamma_digital)
            code_lettersSh = make_letters(code_digitalSh)

        if text_to_code == code_lettersSh:
            status = 'Ok'
        else:
            status = 'Ошибка'

        txts = text_to_code + '\t'
        gammas = gamma_letters + '\t'
        results = code_letters + '\t'
        shifrs = code_lettersSh + '\t'
        statuss = status + '\n'

        # Запись в файл
        file = open('Tests.txt', 'a')
        file.write(txts)
        file.close()

        file = open('Tests.txt', 'a')
        file.write(gammas)
        file.close()

        file = open('Tests.txt', 'a')
        file.write(results)
        file.close()

        file = open('Tests.txt', 'a')
        file.write(shifrs)
        file.close()

        file = open('Tests.txt', 'a')
        file.write(statuss)
        file.close()

    tkinter.messagebox.showinfo('Отчет', message='Результаты тестов сохранены в файл Tests.txt')

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
label2 = Label(frame1, text='Криптограмма:', bg='#E7E6E6', font="Verdana 11")
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
label3.place(x=30, y=365, width=70, height=25)
libEntry = Entry(frame1, bg="white", bd=0, font="Verdana 11")
libEntry.insert(END, 'dictionary.txt')
libEntry.place(x=120, y=365, width=120, height=25)
dict_path=libEntry.get()
# btnOpenD = Button(frame1, bg='white', bd=0, font="Verdana 11")
# btnOpenD.place(x=260, y=335, width=110, height=25)
# btnOpenD['text'] = 'Открыть'
# btnOpenD.bind('<Button-1>', open_dictionary)

# label4 = Label(frame1, text='Гамма:', bg='#E7E6E6', font="Verdana 11")
# label4.place(x=30, y=365, width=60, height=25)
# libEntry2 = Entry(frame1, bg="white", bd=0, font="Verdana 11")
# libEntry2.insert(END, 'gamma.txt')
# libEntry2.place(x=120, y=365, width=120, height=25)
# btnOpenG = Button(frame1, bg='white', bd=0, font="Verdana 11")
# btnOpenG.place(x=260, y=365, width=110, height=25)
# btnOpenG['text'] = 'Открыть'
# btnOpenG.bind('<Button-1>', open_gamma)

btnCod = Button(frame1, bg='white', bd=0, font="Verdana 11")
btnCod.place(x=260, y=263, width=110, height=25)
btnCod['text'] = 'Кодировать'
btnCod.bind('<Button-1>', coding_click)
btnDec = Button(frame1, width=14, bg='white', font="Verdana 11")
btnDec.place(x=410, y=263, width=110, height=25)
btnDec['text'] = 'Декодировать'
btnDec.bind('<Button-1>', decoding_click)

btnTest = Button(frame1, bg='white', font="Verdana 11")
btnTest.place(x=410, y=365, width=130, height=25)
btnTest['text'] = 'Тест шифратора'
btnTest.bind('<Button-1>', test_dialog)

btnClear = Button(frame1, bg='white', font="Verdana 11")
btnClear.place(x=650, y=300, width=100)
btnClear['text'] = 'Очистить'
btnClear.bind('<Button-1>', clear)

window.mainloop()

