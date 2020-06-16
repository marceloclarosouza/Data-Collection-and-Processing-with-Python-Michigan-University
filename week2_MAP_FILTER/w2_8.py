# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:27:26 2020

@author: mcsbi
"""
"""
Define longwords using manual accumulation.
"""
"""Return a shorter list of strings containing only the strings with more
    than four characters. Use manual accumulation."""

def longwords(strings):
    four = []
    for words in strings:
        if len(words) > 4:
            four.append(words)
    return four        
    
strings = ["kashfhf", "klejgwjhfo", "ashfio", "osdhoishd", "ojo", "hih", "ihihio"]

print(longwords(strings))