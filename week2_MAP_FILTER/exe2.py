# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 09:30:01 2020

@author: mcsbi
"""
"""
Below, we have provided a list of strings called abbrevs. Use map to produce 
a new list called abbrevs_upper that contains all the same strings in upper 
case.
"""

abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]


abbrevs_upper = map(lambda st: st.upper(), abbrevs)
print(abbrevs_upper)