#!/usr/bin/env python

import re

numbers = []
with open('file.txt', 'r') as file:
    for line in file:
        numbers.append(int(line))
c,count=0,0
while True:
    try:
        old = c
        c = c + numbers[c]
        if numbers[old] > 2:
            numbers[old] = numbers[old] - 1
        else:
            numbers[old] = numbers[old] + 1
        count = count + 1
    except:
        break

print(count)
