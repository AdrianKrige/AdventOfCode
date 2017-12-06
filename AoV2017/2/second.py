#!/usr/bin/env python

import re
import time

with open('file2.txt', 'r') as file:
    n = 0
    for line in file:
        digits = sorted([int(i) for i in re.split(r'\t+', line.strip())])
        for i in digits:
            mult = i
            while int(mult) < int(digits[-1]):
                mult = int(mult) + int(i)
                if mult in digits:
                    n = n + (mult)/int(i)
                    break
print(n)

