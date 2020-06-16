# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:31:35 2020

@author: mcsbi
"""
"""
Define longwords using filter.
"""

def longwords_Fil(strings):
    long = filter(lambda x: len(x)>4, strings)
    return long
    
strings = ["kashfhf", "klejgwjhfo", "ashfio", "osdhoishd", "ojo", "hih", "ihihio"]

print(longwords_Fil(strings))