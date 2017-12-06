#!/usr/bin/env python

import math

n = 325489

square = n
while True:
  root = math.sqrt(square)
  if root%1 == 0 and root%2 == 1:
      break
  square = square + 1

diff = (square - n)%root
middle = root//2

ans = abs(diff - middle) + (root//2)
