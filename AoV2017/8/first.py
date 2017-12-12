#!/usr/bin/env python

from collections import defaultdict

registers = defaultdict(int)
flag = True
m = 0
with open('file.txt', 'r') as file:
    for line in file:
        elements = line.strip().split(' ')
        reg = elements[0]
        inc = '+' if elements[1][0] == 'i' else '-'
        value = elements[2]
        f_register = elements[4]
        f_compare = elements[5]
        f_value = elements[6]
        f = "{}{}{}".format(registers[f_register],f_compare, f_value)
        if eval(f):
            registers[reg] = eval("{}{}{}".format(registers[reg], inc, value))
            if registers[reg] > m:
                m = registers[reg]
print(max(registers.values()))
print(m)
