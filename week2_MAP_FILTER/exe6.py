# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 12:03:12 2020

@author: mcsbi
"""

"""
Write code to assign to the variable compri all the values of the key name
 in any of the sub-dictionaries in the dictionary tester. Do this using 
 a list comprehension.
"""
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

new_list = tester['info']
import json
print(json.dumps(new_list, indent = 2))

compri = [name['name'] for name in new_list]
print(compri)