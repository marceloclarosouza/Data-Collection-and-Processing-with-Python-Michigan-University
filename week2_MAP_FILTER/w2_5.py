# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:53:16 2020

@author: mcsbi
"""
"""
Write a function called positives_Acc that receives list of numbers as the 
input (like [3, -1, 5, 7]) and returns a list of only the positive numbers, 
[3, 5, 7], via manual accumulation.
"""

things = [3, 5, -4, 7]

def positives_Acc(things):
    positive = [x for x in things if x >= 0]
    return positive

print(positives_Acc(things))