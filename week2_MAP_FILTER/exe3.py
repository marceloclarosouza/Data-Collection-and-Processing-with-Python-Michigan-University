# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:50:20 2020

@author: mcsbi
"""

"""
Write code to assign to the variable filter_testing all the elements in 
lst_check that have a w in them using filter."
"""
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing= list(filter(lambda word: "w" in word, lst_check))
print(filter_testing)