# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:49:55 2020

@author: mcsbi
"""
"""
Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.
"""
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]


pop_info = [(x) for x in zip(species, population)]
print(pop_info)

endangered = [x[0] for x in pop_info if (x[1] < 2500)]
print(endangered)

