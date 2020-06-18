# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:54:33 2020

@author: mcsbi
"""
import requests
import json

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {}# Set up an empty dictionary for query parameters
    params_diction['rel_rhy'] = word
    params_diction['max'] = '3'# get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    
    word_ds = resp.json()
    return[d['word'] for d in word_ds]
    return resp.json()# Return a python object (a list of dictionaries in this case)

print(get_rhymes("cat"))

