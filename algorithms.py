# -*- coding: utf-8 -*-
import random

def get_lst(txt2cod):  # вывести в algorithms
    txt = txt2cod.get('1.0', 'end-1c')
    cod_txt = txt
    return cod_txt

def load_dict(libEntry):
    dict_path=libEntry.get()
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

def get_lst_letters(lst_numbers, dict_digital):
    lst_numbers_str = lst_numbers.split()
    lst_numbers = []
    try:
        for i in lst_numbers_str:
            lst_number = int(i)
            lst_numbers.append(lst_number)

        list_letters = list(dict_digital)
        lst = []
        for i in lst_numbers:
            element = list_letters[i]
            lst.append(element)
        lst_str = ''.join(lst)

    except:
        lst_str = ''

    return lst_str

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

def make_letters(code_digital, libEntry):
    dict_letters = load_dict(libEntry)[1]
    list_letters = list(dict_letters)
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

def make_numbers(code_digital, libEntry):
    dict_letters = load_dict(libEntry)[1]
    list_letters = list(dict_letters)
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
            element = list_letters.index(i)
            code_letters.append(element)
    except KeyError:
        code_letters = []
    return code_letters


def get_criteria(text_to_code, gamma_dig, shifr, libEntry):
    dict_digital = load_dict(libEntry)[0]

    # lst_dig = lst_digital(lst, dict_digital)

    lst = get_lst_letters(shifr, dict_digital)
    if lst == '':
        pass
    else:
        gamma_digital = gamma_dig
        lst_dig = lst_digital(lst, dict_digital)
        code_digital = make_code(lst_dig, gamma_digital)
        code_letters = make_letters(code_digital, libEntry)

    return code_letters == text_to_code

# if __name__ == '__main__':  Нужен ли в algorithms?
