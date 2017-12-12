#!/usr/bin/env python

level = 1
total = 0
offset = 0
garbage = False
pieces = 0
with open('file.txt', 'r') as file:
    for line in file:
        for index in range(len(line)-1):
            try:
                # Check that c is a legit character
                c = line[index+offset]
                if c == '!':
                    offset = offset + 1
                    continue
                
                elif c == '>':
                    garbage = False
                elif garbage:
                    pieces = pieces + 1
                    continue
                elif c == '<':
                    garbage = True
                elif c == '{':
                    total = total + level
                    level = level + 1
                elif c == '}':
                    level = level - 1
                else:
                    pass
            except:
                break
print(pieces) 
