#!/usr/bin/env python
n = input()
digits = [int(x) for x in str(n)]
sum = 0
l = len(digits)
for i in range(l):
    if digits[i] == digits[(i + (l/2))%l]:
        sum = sum + digits[i]
print(sum)
