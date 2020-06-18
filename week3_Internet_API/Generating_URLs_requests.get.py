# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:45:02 2020

@author: mcsbi
"""

import requests
# page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
kval_pairs = {'rel_rhy': 'funny'}
page = requests.get("https://api.datamuse.com/words", params = kval_pairs)
print(page.text[:150])#print the first 150 chars
print(page.url) #print the url that was fetched