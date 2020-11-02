# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.filedialog, tkinter.messagebox

from testX import *


class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Шифратор и дешифратор на основе алгоритма «Блокнот»")
        self.parent.iconbitmap(u'main.ico')
        self.parent.resizable(width=False, height=False)
        self.parent.configure() # Что значит?

        frame1 = Frame(self.parent, width=780, height=410, bg='#E7E6E6')
        frame1.grid(row=0, column=0)
        label1 = Label(frame1, text='Исходный текст:', bg='#E7E6E6', font="Verdana 11")
        label1.place(x=30, y=10, width=340)
        self.txt2cod = Text(frame1, bg='white', font="Verdana 11", wrap=WORD)
        self.txt2cod.config(state=NORMAL)
        self.txt2cod.place(x=30, y=35, width=340, height=220)
        label2 = Label(frame1, text='Криптограмма:', bg='#E7E6E6', font="Verdana 11")
        label2.place(x=410, y=10, width=340)
        self.output = Text(frame1, bg="white", font="Verdana 11", wrap=WORD)
        self.output.config(state=NORMAL)
        self.output.place(x=410, y=35, width=340, height=220)

        btnCod = Button(frame1, bg='white', bd=0, font="Verdana 11")
        btnCod.place(x=260, y=263, width=110, height=25)
        btnCod['text'] = 'Кодировать'
        btnCod.bind('<Button-1>', self.coding_click)
        btnDec = Button(frame1, width=14, bg='white', font="Verdana 11")
        btnDec.place(x=410, y=263, width=110, height=25)
        btnDec['text'] = 'Декодировать'
        btnDec.bind('<Button-1>', self.decoding_click)

        btnClear = Button(frame1, bg='white', font="Verdana 11")
        btnClear.place(x=650, y=300, width=100)
        btnClear['text'] = 'Очистить'
        btnClear.bind('<Button-1>', self.clear)

        btnLoad = Button(frame1, bg='white', bd=0, font="Verdana 11")
        btnLoad.place(x=30, y=263, width=150, height=20)
        btnLoad['text'] = 'Загрузить текст'
        btnLoad.bind('<Button-1>', self.load_text)

        btnSave = Button(frame1, bg='white', bd=0, font="Verdana 11")
        btnSave.place(x=600, y=263, width=150, height=20)
        btnSave['text'] = 'Сохранить результат'
        btnSave.bind('<Button-1>', self.save_text)

        btnTest = Button(frame1, bg='white', font="Verdana 11")
        btnTest.place(x=410, y=365, width=130, height=25)
        btnTest['text'] = 'Тест шифратора'
        btnTest.bind('<Button-1>', self.test_dialog)

        label3 = Label(frame1, text='Словарь:', bg='#E7E6E6', font="Verdana 11")
        label3.place(x=30, y=365, width=70, height=25)
        self.libEntry = Entry(frame1, bg="white", bd=0, font="Verdana 11")
        self.libEntry.insert(END, 'dictionary.txt')
        self.libEntry.place(x=120, y=365, width=120, height=25)

    def load_text(self, event):
        self.filename = tkinter.filedialog.askopenfilename()
        if not (self.filename == ''):
            f = open(self.filename, 'r')
            f2 = f.read()
            f.close()
            self.txt2cod.delete('1.0', 'end')
            self.txt2cod.insert("0.0", f2)

    def coding_click(self, event):
        lst = get_lst(self.txt2cod)
        dict_digital = load_dict(self.libEntry)[0]
        lst_dig = lst_digital(lst, dict_digital)
        if lst_dig == []:
            self.output.delete('1.0', 'end')
            self.output.insert('0.0', 'Невозможно зашифровать символ исходного текста')
        else:
            gamma_digital = get_gamma(lst)
            code_digital = make_code(lst_dig, gamma_digital)
            code_numbers = make_numbers(code_digital, self.libEntry)
            self.output.delete('1.0', 'end')
            self.output.insert("0.0", code_numbers)

    def decoding_click(self, event):
        code_numbers = self.output.get('1.0', 'end-1c')
        self.txt2cod.delete('1.0', 'end')
        self.txt2cod.insert('0.0', code_numbers)
        dict_digital = load_dict(self.libEntry)[0]
        lst = get_lst_letters(code_numbers, dict_digital)
        if lst == '':
            self.output.delete('1.0', 'end')
            self.output.insert('0.0', 'Невозможно дешифровать криптограмму, так как в криптограмме используется недопустимое значение')
        else:
            lst_dig = lst_digital(lst, dict_digital)
            gamma_file = 'gamma.txt'
            file = open(gamma_file, 'r', encoding="utf8")
            gamma_digital = file.read()
            file.close()

            code_digital = make_code(lst_dig, gamma_digital)
            code_letters = make_letters(code_digital, self.libEntry)
            self.output.delete('1.0', 'end')
            self.output.insert("0.0", code_letters)

    def clear(self, event):
        self.output.delete('1.0', 'end')
        self.txt2cod.delete('1.0', 'end')

    def save_text(self, event):
        txt = self.txt2cod.get('1.0', 'end-1c')
        shifr = self.output.get('1.0', 'end-1c')
        if txt == '':
            tkinter.messagebox.showinfo('Уведомление', message='Нет текста / криптограммы для сохранения в файл')
        elif txt != '' and shifr=='':
            tkinter.messagebox.showinfo('Уведомление', message='Проведите кодирование текста, после чего сохраните результат в файл')
        else:
            gamma_file = 'gamma.txt'
            file = open(gamma_file, 'r', encoding="utf8")
            gamma_dig = file.read()
            file.close()

            criteria = get_criteria (txt, gamma_dig, shifr, self.libEntry)
            if not criteria:
                tkinter.messagebox.showinfo('Уведомление',
                                            message='Текст и криптограмма не соответсвтуют друг другу. Проведите кодирование текста, после чего сохраните результат в файл')
            else:
                dict_digital = load_dict(self.libEntry)[0]
                txt_dig = lst_digital(txt, dict_digital)
                txts = 'Исходный текст: ' + txt + ' ({})'.format(txt_dig)

                gamma_letters = make_letters(gamma_dig, self.libEntry)
                gammas = 'Гамма: ' + gamma_dig + ' ({})'.format(gamma_letters) + '\n'

                result = self.output.get('0.0', 'end-1c')
                dict_digital = load_dict(self.libEntry)[0]
                result_letters = get_lst_letters(result, dict_digital)
                result_dig = lst_digital(result_letters, dict_digital)
                results = 'Результат: ' + result + ' ({})'.format(result_dig) + ' ({})'.format(result_letters) + '\n'

                file = open('results.txt', 'w')
                file.write(results)
                file.close()

                file = open('results.txt', 'a')
                file.write(gammas)
                file.close()

                file = open('results.txt', 'a')
                file.write(txts)
                file.close()
                tkinter.messagebox.showinfo('Уведомление', message='Текст, гамма и криптограмма сохранены в файл results.txt')

    def test_dialog(self, event):
        root = Tk()
        app = Test(root)
        app.mainloop()

def main():
    root = Tk()
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()