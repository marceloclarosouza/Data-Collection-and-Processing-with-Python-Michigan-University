# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:45:35 2020

@author: mcsbi
"""
"""
Now define lengths using map instead.
"""
def lengths(strings):
    length = map(lambda x : len(x), strings)
    return length

strings = ['aaa', 'bbbccc', 'crerertcc']
print(lengths(strings))

