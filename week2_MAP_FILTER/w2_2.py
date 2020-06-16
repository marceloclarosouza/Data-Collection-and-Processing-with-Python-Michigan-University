# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:14:04 2020

@author: mcsbi
"""
"""
Use manual accumulation to define the lengths function below.
"""
def lengths(strings):
    new_list = []
    for word in strings:
        new_list.append(len(word))
    return new_list

strings = ['aaa', 'bbbccc', 'crerertcc']

print(lengths(strings))