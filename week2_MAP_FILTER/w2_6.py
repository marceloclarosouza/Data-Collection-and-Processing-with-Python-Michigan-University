# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:56:58 2020

@author: mcsbi
"""
"""
Write a function called positives_Fil that receives list of things as the 
input and returns a list of only the positive things, [3, 5, 7], using 
the filter function
"""

things = [3, 5, -4, 7]

def positives_Fil(things):
    positive = filter(lambda x: x >=0, things)
    return positive
    
print(positives_Fil(things))