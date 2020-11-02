# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.filedialog, tkinter.messagebox
from algorithms import *
import random

class Test(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white") # Зачем это нужно?
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Тест шифратора")
        self.parent.iconbitmap(u'main.ico')
        self.parent.resizable(width=False, height=False)
        self.parent.configure()

        frameT = Frame(self.parent, width=340, height=220, bg='#E7E6E6')
        frameT.grid(row=0, column=0)

        labelT1 = Label(frameT, text='Количество тестов:', bg='#E7E6E6', font="Verdana 11")
        labelT1.place(x=10, y=30, width=150, height=25)
        self.libEntryT1 = Entry(frameT, bg="white", bd=0, font="Verdana 11")
        self.libEntryT1.insert(END, 7)
        self.libEntryT1.place(x=250, y=30, width=60, height=25)

        labelT2 = Label(frameT, text='Max длина текста:', bg='#E7E6E6', font="Verdana 11")
        labelT2.place(x=10, y=75, width=150, height=25)
        self.libEntryT2 = Entry(frameT, bg="white", bd=0, font="Verdana 11")
        self.libEntryT2.insert(END, 7)
        self.libEntryT2.place(x=250, y=75, width=60, height=25)

        labelT3 = Label(frameT, text='Словарь:', bg='#E7E6E6', font="Verdana 11")
        labelT3.place(x=10, y=120, width=150, height=25)
        self.libEntryT3 = Entry(frameT, bg="white", bd=0, font="Verdana 11")
        self.libEntryT3.insert(END, 'dictionary.txt')
        self.libEntryT3.place(x=190, y=120, width=120, height=25)

        btnTest = Button(frameT, bg='white', bd=0, font="Verdana 11")
        btnTest.place(x=200, y=180, width=110, height=25)
        btnTest['text'] = 'Начать тест'
        btnTest.bind('<Button-1>', self.testing_click)

    def testing_click(self, event):
        tests_count = int(self.libEntryT1.get())
        text_length = int(self.libEntryT2.get())

        file_name = 'Tests.txt'
        # Очистить файл
        file = open(file_name, 'w')
        file.write('Результаты тестов' + ' ({}'.format(tests_count) + ' шт.):' + '\n')
        file.close()

        # Подготовка словаря
        dict_digital = load_dict(self.libEntryT3)[0]
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
            if lst_dig == '':
                tkinter.messagebox.showinfo('Ошибка', message='Не удалось перевести текст в двоичный код:'+ ' ({})'.format(lst))
                pass
            else:
                gamma_digital = get_gamma(lst)
                gamma_letters = make_letters(gamma_digital, self.libEntryT3)
                code_digital = make_code(lst_dig, gamma_digital)
                code_numbers = make_numbers(code_digital, self.libEntryT3)
                code_numbers_str = ' '.join(str(j) for j in code_numbers)

                shifr_letters = get_lst_letters(code_numbers_str, dict_digital)
                shifr_dig = lst_digital(shifr_letters, dict_digital)
                shifr_digital = make_code(shifr_dig, gamma_digital)
                shifr_letters = make_letters(shifr_digital, self.libEntryT3)

                status = text_to_code == shifr_letters

                test_num = str(test_number) + '\t'
                test_length = str(text_len) + '\t'
                txts = text_to_code + ' ({})'.format(lst_dig) + '\t'
                gammas = gamma_letters + ' ({})'.format(gamma_digital) + '\t'
                results = code_numbers_str + ' ({})'.format(code_digital) + '\t'
                shifrs = shifr_letters + '\t'
                statuss = str(status) + '\n'

                # Запись в файл
                file = open(file_name, 'a')
                file.write(test_num)
                file.close()

                file = open(file_name, 'a')
                file.write(test_length)
                file.close()

                file = open(file_name, 'a')
                file.write(txts)
                file.close()

                file = open(file_name, 'a')
                file.write(gammas)
                file.close()

                file = open(file_name, 'a')
                file.write(results)
                file.close()

                file = open(file_name, 'a')
                file.write(shifrs)
                file.close()

                file = open(file_name, 'a')
                file.write(statuss)
                file.close()

        tkinter.messagebox.showinfo('Отчет', message='Результаты тестов сохранены в файл Tests.txt')
