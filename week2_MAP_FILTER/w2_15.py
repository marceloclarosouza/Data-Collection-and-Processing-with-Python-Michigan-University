# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:12:11 2020

@author: mcsbi
"""
"""
Use the zip function to take the lists below and turn them into a list of 
tuples, with all the first items in the first tuple, etc.
"""

L1 = [1, 2, 3, 4]
L2 = [4, 3, 2, 3]
L3 = [0, 5, 0, 5]
L4 = list(zip(L1, L2, L3))
tups = []

for x in L4:
    tups.append(x)

print(tups)