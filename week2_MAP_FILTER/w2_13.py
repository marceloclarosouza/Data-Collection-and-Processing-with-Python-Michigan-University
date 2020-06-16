# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:00:05 2020

@author: mcsbi
"""
"""
Write a function that takes a list of numbers and returns the sum of the 
squares of all the numbers. Try it using an accumulator pattern.
"""

def sumSquares(L):
    count = 0
    
    for nums in L:
        count += nums**2
    return count

nums = [3, 2, 2, -1, 1]

print(sumSquares(nums))