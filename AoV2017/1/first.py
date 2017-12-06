#!/usr/bin/env python
n = input()
digits = [int(x) for x in str(n)]
digits.append(digits[0])
sum = 0
for i in range(len(digits) - 1):
    if digits[i] == digits[i+1]:
        sum = sum + digits[i]
print(sum)
