#!/usr/bin/python3

list_1 = ['1123aaaare21\n', 'AAAAA11213ZZZ\n', '232fdfD321\n', '21sdsss1\n']


print(sorted([(ix, ''.join(j for j in line if j.isalpha()), ''.join(j for j in line if j.isalpha()
        ).isupper(), sum(map(int, ''.join(s if s.isdigit() else ' ' for s in line
        ).split()))) for ix, line in enumerate(list_1)], key=lambda x:x[3]))


