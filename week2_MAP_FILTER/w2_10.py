# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:34:23 2020

@author: mcsbi
"""

"""
Define longwords using a list comprehension.
"""

def longwords_Li_Comp(strings):
    long = [x for x in strings if len(x) >4]
    return long  
    
    
strings = ["kashfhf", "klejgwjhfo", "ashfio", "osdhoishd", "ojo", "hih", "ihihio"]
print(longwords_Li_Comp(strings))