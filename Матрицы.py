#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Wed Nov  1 10:11:37 2017.

@author: lashkov

"""
# Ввод матрицы
M = []
while True:
    try:
        N = int(input('Введите число строк равное числу столбцов матрицы: '))
        if N < 1:
            raise ValueError('Чиcло должно быть больше 0!')
    except ValueError as e:
        print('Ошибка! {:s} Введите корректное значение!'.format(str(e)))
    else:
        break
for i in range(1, N + 1):
    S = []
    for j in range(1, N + 1):
        while True:
            try:
                e = float(input(
                    'Введите значение для строки № {0:d}, столбца № {1:d}): '.format(i, j)))
            except ValueError:
                print('Ошибка! Введите корректное значение!')
            else:
                break
        S.append(e)
    M.append(S)

# Вывод 6 символов на число, восемь на ячейку
print('\u250c' + ('\u2500' * 8 + '\u252c') * (N - 1) + '\u2500' * 8 + '\u2510')
for i, S in enumerate(M):
    print('\u2502', end='')
    for e in S:
        print(' {:^6.2g} \u2502'.format(e), end='')
    print()
    if i + 1 < N:
        print('\u251c' + ('\u2500' * 8 + '\u253c')
              * (N - 1) + '\u2500' * 8 + '\u2524')
print('\u2514' + ('\u2500' * 8 + '\u2534') * (N - 1) + '\u2500' * 8 + '\u2518')

# Вывод номера строк с минимальным и максимальным количеством отрицательных элементов
neg_list_n = []
for S in M:
    n = 0
    for e in S:
        if e < 0:
            n += 1
    neg_list_n.append(n)
if neg_list_n.count(0) == len(neg_list_n):
    print('Нет строк с отрицательными элементами!!!')
else:
    print('Строка с минимальным количеством отрицательных элементов: {:d})'.format(
        neg_list_n.index(min(neg_list_n)) + 1))
    print('Строка с максимальным количеством отрицательных элементов: {:d})'.format(
        neg_list_n.index(max(neg_list_n)) + 1))

# Поддиагональные элементы матрицы
D = []
for i, S in enumerate(M):
    for j, e in enumerate(S):
        if j < i:
            D.append(e)
if D:
    print('Поддиагональные элементы матрицы: ', D)
else:
    print('Матрица из одного элемента')

input()
