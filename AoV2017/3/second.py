#!/usr/bin/env python
import math

def larger_odd_square(n):
    while True:
        n = n + 1
        root = math.sqrt(n)
        if root%1 == 0 and root%2 == 1:
            return n


def add_for_square(count, n):
    #print(count)
    #print(n)
    pass


d = {0:1, }
count = 1
n = 0
while count < 40:
    # Only calculate when we need to.
    old, n = n, larger_odd_square(count)
    print(n)
    print(old)
    print(count)
    print()
    for x in range(n-1):
        add_for_square(count, n)
        count = count + 1


