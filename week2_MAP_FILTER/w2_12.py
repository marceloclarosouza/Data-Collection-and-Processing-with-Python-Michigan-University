# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:41:59 2020

@author: mcsbi
"""
"""
Write a function called longlengths that returns the lengths of those strings
 that have at least 4 characters. Try it using map and filter.
"""

def longlengths(strings):
    long = list(filter(lambda x: len(x) >=4, strings))
    l_map = list(map(lambda x: len(x), long))
    return l_map

strings = ["kashfhf", "klejgwjhfo", "ashfio", "osdhoishd", "ojo", "hih", "ihihio"]
print(longlengths(strings))