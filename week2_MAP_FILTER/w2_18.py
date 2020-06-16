# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:02:23 2020

@author: mcsbi
"""
"""
Challenge: The nested for loop given takes in a list of lists and combines 
the elements into a single list. Do the same thing using a list comprehension
 for the list L. Assign it to the variable result2.
"""

def onelist(lst):
    result = []
    for each_list in lst:
        for item in each_list:
            result.append(item)
    return result

L = [["hi", "bye"], ["hello", "goodbye"], ["hola", "adios", "bonjour", "au revoir"]]


result2 = [item for lst in L for item in lst]
print(result2)
