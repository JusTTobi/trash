#!/usr/bin/python3
import sys

filename = sys.argv[1]
try:
    with open(filename) as file_pdb:
        s_array = file_pdb.readlines()
except FileNotFoundError:
    print('Файл {s} не найлен!'.format(filename))
    sys.exit(1)
o_array = []
n = 1
for s in s_array:
    if (s[0:6] == 'ATOM  ' or s[0:6] == 'HETATM') and not (s[76:78] == ' H' or s[76:78] == '  '):
        o_array.append(s)
    elif s[0:5] == 'MODEL':
        o_array.append("MODEL {0:8d}\n".format(n))
        n += 1
    elif s[0:6] == 'ENDMDL':
        o_array.append(s)
o_array.append('END\n')

try:
    with open(filename.split('.')[0] + '_md.pdb', 'w') as file_pdb:
        file_pdb.writelines(o_array)
except IOError:
    print('Ошибка ввода-вывода!')
    sys.exit(1)
