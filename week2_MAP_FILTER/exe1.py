# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:08:07 2020

@author: mcsbi
"""
"""
Using map, create a list assigned to the variable greeting_doubled that 
doubles each element in the list lst.
"""

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled = map(lambda st: 2*st, lst)
print(greeting_doubled)