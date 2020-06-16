# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:02:42 2020

@author: mcsbi
"""

"""
Write a function that takes a list of numbers and returns the sum of the 
squares of all the numbers. Try it using map and sum.
"""
def sumSquares(L):
    
    num = list(map(lambda x: (x*x), L))
    s_num = sum(num) 
    return s_num

nums = [3, 2, 2, -1, 1]
print(sumSquares(nums))
