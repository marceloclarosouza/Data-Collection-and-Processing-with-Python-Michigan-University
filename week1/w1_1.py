# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:08:51 2020

@author: mcsbi
"""

"""
Assign ‘snake’ to the variable output using indexing.
"""
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]

for lst in nested:
    for animals in lst:
        if animals == 'snake':
            output = 'snake'
print(output)