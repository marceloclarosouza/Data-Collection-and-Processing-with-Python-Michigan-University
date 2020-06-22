# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 08:51:16 2020

@author: mcsbi
"""
"""
Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.
"""

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing= list(map(lambda word: "Fruit: " + word, lst_check))
print(map_testing)