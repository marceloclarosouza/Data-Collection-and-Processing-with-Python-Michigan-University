# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:33:45 2020

@author: mcsbi
"""


#Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]

b_strings =[]

for data in L:
    for fruits in data:        
        if 'b' in fruits:
            b_strings.append(fruits)
print(b_strings)