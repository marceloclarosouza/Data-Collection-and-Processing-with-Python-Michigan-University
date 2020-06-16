# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:37:44 2020

@author: mcsbi
"""
"""
Write a function called longlengths that returns the lengths of those
 strings that have at least 4 characters. Try it with a list comprehension
"""

def longlengths(strings):
    long = [len(x) for x in strings if len(x) >= 4]
    return long

strings = ["kashfhf", "klejgwjhfo", "ashfio", "osdhoishd", "ojo", "hih", "ihihio"]
print(longlengths(strings))