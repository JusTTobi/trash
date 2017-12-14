#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:19:23 2017

@author: lashkov
"""

import sys
import numpy as np
import math


def random_plus(orig_xyz, std_dev, n):
    noise = np.random.normal(scale=std_dev, size=3) * (math.sin(n * float(sys.argv[4]))) ** 2
    return orig_xyz + noise


old_file = sys.argv[1]
new_file = sys.argv[2]
with open(old_file) as of:
    lines = of.readlines()
nf = open(new_file, 'a')
n = 0
for line in lines:
    if line[0:5] == 'MODEL':
        s = 'MODEL' + '{0:9d}'.format(n) + '\n'
    elif line[0:6] == "HETATM" or line[0:6] == "ATOM  ":
        xyz = [float(line[30:38]), float(line[38:46]), float(line[46:54])]
        xyz_mod = random_plus(xyz, float(sys.argv[3]), n)
        s = line[0:30] + '{0:>8.3f}{1:>8.3f}{2:>8.3f}'.format(list(xyz_mod)[0], list(xyz_mod)[1],
                                                              list(xyz_mod)[2]) + line[54:]
    elif line[0:6] == 'ENDMDL':
        n += 1
        s = line[:]
    else:
        s = line[:]
    print(s)
    nf.write(s)
nf.close()
