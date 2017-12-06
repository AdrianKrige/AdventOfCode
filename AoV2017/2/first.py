#!/usr/bin/env python

import re

with open('file.txt', 'r') as file:
    n = 0
    for line in file:
        digits = re.split(r'\t+', line)
        #digits = line.strip().split('\t')
        max_n, min_n = max([int(i) for i in digits]), min([int(x) for x in digits])
        print("MAx: {} , min: {}".format(max_n, min_n))
        n =  n + (int(max_n) - int(min_n))
print(n)
