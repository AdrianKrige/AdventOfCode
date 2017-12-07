#!/usr/bin/env python

nodes = {}
with open('file2.txt', 'r') as file:
    for line in file:
        parent = line.split(')')[0].strip()
        children = []
        try:
            children = line.split('->')[1].strip().split(', ')
            nodes[parent] = children
        except:
            nodes[parent] = children

node_weights = {}
for name in nodes.keys():
    n = name.split('(')[0].strip()
    weight = name.split('(')[1]
    node_weights[n] = weight


class Node:
    def __init__(self, name=None, weight=None, parent=None):
        self.weight = weight
        self.parent = parent
        self.children = []
        self.name = name

    def add_child(self, child):
        self.children.append(child)


Nodes = {}
for name, children in nodes.items():
    parent_name = name.split('(')[0].strip()
    parent = None
    try:
        parent = Nodes[parent_name]
    except:
        parent = Node(parent_name, node_weights[parent_name], None)
    Nodes[parent_name] = parent
    for child in children:
        try:
            child_node = Nodes[child]
        except:
            child_node = Node(child, node_weights[child], parent)
        parent.add_child(child_node)


# #DEBUG - Print all info
# for name, node in Nodes.items():
#     print(name)
#     print(parent.name)
#     print(node.weight)
#     print([child.name for child in node.children])
#     print

p = Nodes['eugwuhl']
# p = Nodes['tknk']


def rec_sum(node):
    return int(node.weight) + sum(rec_sum(child) for child in node.children)

sums = {}
for c in p.children:
    sums[c.name] = rec_sum(c)

print(sums)



