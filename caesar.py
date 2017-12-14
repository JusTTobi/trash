#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:56:14 2017

@author: lashkov
"""

L1 = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
L2 = list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')


def inputWk() -> (str, str):
    word = input('Введите фразу: ')
    key = input('Введите ключ: ').lower()
    key_tmp = ''
    for s in key:
        key_tmp += s if s in L1 else ''
    key = key_tmp
    print('Очищенный ключ:', key)
    if key == '': raise ValueError
    return word, key


def cycleShift(L: list, n: int) -> list:
    L = L[:]
    i = 0
    while i < n:
        el = L.pop(0)
        L.append(el)
        i += 1
    return L


def cycleUnshift(L: list, n: int) -> list:
    L = L[:]
    i = 0
    while i < n:
        el = L.pop()
        L.insert(0, el)
        i += 1
    return L


def keyEl(key: str, n: int) -> str:
    return key[n % len(key)]


def crypt(word: str, key: str) -> str:
    crypt_txt = ''
    n = 0
    for s in word:
        if s in L1:
            crypt_txt += cycleShift(L1, L1.index(keyEl(key, n)))[L1.index(s)]
            n += 1
        elif s in L2:
            crypt_txt += cycleShift(L2, L1.index(keyEl(key, n)))[L2.index(s)]
            n += 1
        else:
            crypt_txt += s
    return crypt_txt


def decrypt(word: str, key: str) -> str:
    crypt_txt = ''
    n = 0
    for s in word:
        if s in L1:
            crypt_txt += cycleUnshift(L1, L1.index(keyEl(key, n)))[L1.index(s)]
            n += 1
        elif s in L2:
            crypt_txt += cycleUnshift(L2, L1.index(keyEl(key, n)))[L2.index(s)]
            n += 1
        else:
            crypt_txt += s
    return crypt_txt


def printTable(L1: list):
    print('  ' + ''.join(L1))
    for i, s in enumerate(L1):
        print('{0:s}:{1:s}'.format(s, ''.join(cycleShift(L1, i))))


while True:
    try:
        m = int(input(
            '1 - Напечатать таблицу\n2 - Зашифровать\n3 - Расшифровать\n4 - Выход\nЧто Вы хотите сделать?: '))
        if m < 1 or m > 4:
            raise ValueError
        if m == 1:
            printTable(L1)
        elif m == 2:
            word, key = inputWk()
            print('Зашифрованная фраза:', crypt(word, key))
            continue
        elif m == 3:
            word, key = inputWk()
            print('Расшифрованная фраза:', decrypt(word, key))
            continue
        elif m == 4:
            break
    except ValueError:
        print('Введите корректное значение!')
        continue
    except KeyboardInterrupt:
        break
input('Нажмите Enter!')
