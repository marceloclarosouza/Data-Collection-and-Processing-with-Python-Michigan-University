# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:49:44 2020

@author: mcsbi
"""
"""
Now define lengths using a list comprehension instead.
"""

def lengths(strings):
    length = [len(x) for x in strings]
    return length

strings = ['aaa', 'bbbccc', 'crerertcc']
print(lengths(strings))
