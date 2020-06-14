# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:04:29 2020

@author: mcsbi
"""

"""
Iterate through the contents of l_of_l and assign the third element of 
sublist to a new list called third.
"""
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]

third = []

for lista in l_of_l:
    third.append(lista[2])

print(third)