#!/usr/bin/env python

import re

nodes = {}
Nodes = []


with open('file2.txt', 'r') as file:
    for line in file:
        parent = line.split('(')[0].strip()
        children = []
        try:
            children = line.split('->')[1].strip().split(', ')
            nodes[parent] = children
        except:
            nodes[parent] = children

all_children = []
for name, children in nodes.items():
    all_children = all_children + children

for name in nodes.keys():
    if name not in all_children:
        print(name)
print(all_children)


