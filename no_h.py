#!/usr/bin/python3
import sys
from itertools import filterfalse

def fpdb(s):
    if ((s[0:6] == 'ATOM  ' or s[0:6] == 'HETATM') and s[76:78]) == ' H':
        return True

if len(sys.argv) > 1:
    for n in range(len(sys.argv) - 1):
        filename = sys.argv[n + 1]
        try:
            with open(filename) as file_pdb:
                s_array = file_pdb.readlines()
        except FileNotFoundError:
            print('Файл {s} не найлен!'.format(filename))
            sys.exit(1)
        o_array = filterfalse(fpdb, s_array)
        try:
            with open(filename.split('.')[0] + '_noh.pdb', 'w') as file_pdb:
                file_pdb.writelines(o_array)
        except IOError:
            print('Ошибка ввода-вывода!')
            sys.exit(1)
else:
    sys.exit(1)
