# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 09:51:37 2020

@author: mcsbi
"""
"""
Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.
"""
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [names[1] for names in people]
print(first_names)
