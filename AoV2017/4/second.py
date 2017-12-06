#!/usr/bin/env python

import re

with open('file.txt', 'r') as file:
    n = 0
    for line in file:
        words_list = line.strip().split(' ')
        new = []
        for word in words_list:
            c = list(word)
            new.append(''.join(sorted(c)))
        words_set = set(new)
        if len(words_set) == len(words_list):
            n = n + 1
print(n)
