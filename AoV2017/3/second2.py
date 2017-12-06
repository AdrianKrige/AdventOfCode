#!/usr/bin/env python
from collections import defaultdict

spiral = defaultdict(lambda: defaultdict(int))

spiral[0][0] = 1
count = 1
x, y = 1, 0
larger_than = 325489


def sum_around(cur_x, curr_y):
    vertical_sum = spiral[cur_x][curr_y + 1] + spiral[cur_x][curr_y - 1]
    horizontal_sum = spiral[cur_x + 1][curr_y] + spiral[cur_x - 1][curr_y]
    corners_sum = spiral[cur_x + 1][curr_y + 1] + spiral[cur_x + 1][curr_y - 1] + spiral[cur_x - 1][curr_y + 1] + spiral[cur_x - 1][curr_y - 1]
    total = int(vertical_sum+horizontal_sum+corners_sum)
    if total > larger_than:
        # This is the answer
        print(total)
    return total


for i in range(5):
    # Found a pattern, always:
    # n up; n + 1 left; n + 1 down; n + 2 right
    # for every odd n
    for up in range(count):
        spiral[x][y] = sum_around(x, y)
        y = y + 1
    for left in range(count + 1):
        spiral[x][y] = sum_around(x, y)
        x = x - 1
    for down in range(count + 1):
        spiral[x][y] = sum_around(x, y)
        y = y - 1
    for right in range(count + 2):
        spiral[x][y] = sum_around(x, y)
        x = x + 1
    count = count + 2
