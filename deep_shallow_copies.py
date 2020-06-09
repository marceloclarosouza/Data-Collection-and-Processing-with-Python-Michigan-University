# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 15:54:43 2020

@author: mcsbi
"""


import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]

shallow_copy_version = original [:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("*************originals***********")
print(original)
print("*****************deep copy********")
print(deeply_copied_version)
print("********shallow copy**************")
print(shallow_copy_version)