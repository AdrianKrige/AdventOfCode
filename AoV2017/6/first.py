#!/usr/bin/env python

lists = []
flag = True
with open('test.txt', 'r') as file:
    for line in file:
        stacks = line.strip().split(' ')
stacks = [int(i) for i in stacks]
print(stacks)
l = len(stacks)

while flag:
    lists.append((stacks[:], stacks[0]))
    max_value = max(stacks)
    max_index = stacks.index(max_value)
    stacks[max_index] = 0
    for i in range(max_value):
        stacks[(max_index+1+i)%l] = stacks[(max_index+1+i)%l] + 1
    for index, number in enumerate(lists):
        if number[0] == stacks:
            print("One: {}".format(len(lists)))
            print("Two: {}".format(len(lists) - index))
            flag = False
