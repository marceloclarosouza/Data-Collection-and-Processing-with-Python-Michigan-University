# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:12:14 2020

@author: mcsbi
"""
"""
Write equivalent code using map instead of the manual accumulation below 
and assign it to the variable test.
"""

things = [3, 5, -4, 7]

accum = []
for thing in things:
    accum.append(thing+1)
print(accum)

test = map(lambda x: x + 1, things)
print(test)