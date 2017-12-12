#!/usr/bin/env python3
from collections import deque


def process(q, l=256):
    current, size = 0, 0
    h = [int(i) for i in range(l)]
    l = len(h)
    skip = 0

    while q:
        size = q.popleft()
        for c in range(size // 2):
            left = (current + c) % l
            right = (current + size - c - 1) % l
            h[left], h[right] = h[right], h[left]

        current = (current + size + skip) % l
        skip = skip + 1

    print(h[0] * h[1])


process(deque(int(i) for i in '3415'), 5)
q = deque()
with open('file.txt', 'r') as file:
    for line in file:
        for c in line.strip().split(','):
            q.append(int(c))
process(q)
