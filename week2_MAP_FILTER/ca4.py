# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:02:53 2020

@author: mcsbi
"""
"""
Use list comprehension to create a list called lst2 that doubles each element in the list, lst

"""

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [2*elements for elements in lst]
print(lst2)

