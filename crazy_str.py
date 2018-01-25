#!/usr/bin/python3
from functools import cmp_to_key

list_1 = ['1123aaaare21\n', 'AAAAA11213ZZZ\n', '232fdfD321\n', 'DFFFGG12', '21sdsss1\n']


def func(a, b):
    if a[1] or b[1]:
        return 0
    elif b[2] > a[2]:
        return 1
    elif a[2] < b[2]:
        return -1
    elif a[2] == b[2]:
        return 0


print(sorted([(''.join(j for j in line if j.isalpha()) + '\n', ''.join(
    j for j in line if j.isalpha()).isupper(), sum(map(
    int, ''.join(s if s.isdigit() else ' ' for s in line
    ).split()))) for line in list_1], key=cmp_to_key(func)))
