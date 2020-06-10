# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:38:31 2020

@author: mcsbi
"""


"""Iterate through the list so that if the character ‘m’ is in the string, 
then it should be added to a new list called m_list. Hint: Because this isn’t
 just a list of lists, think about what type of object you want your data to
 be stored in.
"""
d = ['good morning', 'hello', 'chair', 'python', ['music', 'flowers', 'facebook', 'instagram', 'snapchat', ['On my Own', 'monster', 'Words dont come so easily', 'lead me right']], 'Stressed Out', 'Pauver Coeur', 'Reach for Tomorrow', 'mariners song', 'Wonder sleeps here']

m_list = []

for data in d:
    if type(data) is list:
        for lst in data:
            if type(lst) is list:
                for word in lst:
                    if 'm' in word:
                        m_list.append(word)           
            else:
                if 'm' in lst:
                    m_list.append(lst)    
    else:
        if 'm' in data:
            m_list.append(data)
            
print(m_list)