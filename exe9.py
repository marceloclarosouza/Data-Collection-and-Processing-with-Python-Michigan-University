# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:48:35 2020

@author: mcsbi
"""

"""
The nested dictionary, pokemon, shows the number of various Pokemon that 
each person has caught while playing Pokemon Go. Find the total number of 
rattatas, dittos, and pidgeys caught and assign to the variables r, d, and p 
respectively. Do not hardcode. Note: Be aware that not every trainer has 
caught a ditto.
"""
pokemon = {'Trainer1':
          {'normal': {'rattatas':15, 'eevees': 2, 'ditto':1}, 'water': {'magikarps':3}, 'flying': {'zubats':8, 'pidgey': 12}},
          'Trainer2':
          {'normal': {'rattatas':25, 'eevees': 1}, 'water': {'magikarps':7}, 'flying': {'zubats':3, 'pidgey': 15}},
          'Trainer3':
          {'normal': {'rattatas':10, 'eevees': 3, 'ditto':2}, 'water': {'magikarps':2}, 'flying': {'zubats':3, 'pidgey': 20}},
          'Trainer4':
          {'normal': {'rattatas':17, 'eevees': 1}, 'water': {'magikarps':9}, 'flying': {'zubats':12, 'pidgey': 14}}}


p = 0 # pidgeys
r = 0 #rattatas
d = 0 # ditto

for level1 in pokemon.values():
    for level2 in level1.values():
        for level3 in level2:
            if level3 == 'rattatas':
                r += level2['rattatas']
            if level3 == 'ditto':
                d += level2['ditto']
            if level3 == 'pidgey':
                p += level2['pidgey']
                
print("{}, {}, {}".format (p, d, r))













