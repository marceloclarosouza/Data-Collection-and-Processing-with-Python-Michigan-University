# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 09:21:10 2020

@author: mcsbi
"""


#Using indexing, retrieve the string ‘willow’ from the list and assign that to the variable plant.
data = ['bagel', 'cream cheese', 'breakfast', 'grits', 'eggs', 'bacon', [34, 9, 73, []], [['willow', 'birch', 'elm'], 'apple', 'peach', 'cherry']]

plant=data[7][0][0]
print(plant)