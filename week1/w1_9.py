# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 11:11:14 2020

@author: mcsbi
"""

"""
Given below is a list of lists of athletes. Create a list, t, that saves only
 the athlete’s name if it contains the letter “t”. If it does not contain the
 letter “t”, save the athlete name into list other
"""
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]

t = []
other = []

for atletas in athletes:
  for names in atletas:
      if 't' in names:
          t.append(names)
      else:
          other.append(names)
          
print(t, other)