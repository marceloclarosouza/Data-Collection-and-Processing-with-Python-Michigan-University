# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:25:29 2020

@author: mcsbi
"""
"""
Write code to assign to the variable compri_sample all the values of the key 
name in the dictionary tester if they are Juniors. Do this using 
list comprehension.
"""

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}


import json
print(json.dumps(tester['info'], indent = 2))

info = tester['info']
compri_sample = [name['name'] for name in info if name['class standing'] == 'Junior']
print(compri_sample)