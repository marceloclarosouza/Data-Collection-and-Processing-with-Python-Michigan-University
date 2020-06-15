# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:51:40 2020

@author: mcsbi
"""

nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]

for x in nested1:
    print("level1: ")
    if type (x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)
