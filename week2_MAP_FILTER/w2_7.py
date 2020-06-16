# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:25:00 2020

@author: mcsbi
"""

"""
Write a function called positives_Li_Com that receives list of things as
 the input and returns a list of only the positive things, [3, 5, 7], using 
 the list comprehension.
"""
things = [3, 5, -4, 7]

def positives_Li_Com(things):
    positive = [x for x in things if x >=0]
    return positive

print(positives_Li_Com(things))