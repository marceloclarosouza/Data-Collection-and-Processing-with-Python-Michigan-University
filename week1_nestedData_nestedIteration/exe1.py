# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:00:19 2020

@author: mcsbi
"""

#write code to print the value associated with key 'c' in the second dictionary (90)

#write code to print the value associated with key 'b' in the third dictionary

#add a fourth dictionary add the end of the list; print something to check your work.

#change the value associated with 'c' in the third dictionary from "yes" to "no"; print something to check your work

nested2 = [{'a': 1, 'b': 3}, {'a': 5, 'c': 90, 5: 50}, {'b': 3, 'c': "yes"}]

print(nested2[1]['c'])
print(nested2[2]['b'])
nested2.append({'a':2, 'b':3})
nested2[2]['c']="no"
print(nested2)