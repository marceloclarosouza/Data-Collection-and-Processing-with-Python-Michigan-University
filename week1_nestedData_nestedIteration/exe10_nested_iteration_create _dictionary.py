# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:40:36 2020

@author: mcsbi
"""


"""
Use nested iteration to create a dictionary, word_counts, that contains all 
the words in big_list as keys, and the number of times they occur as values.
"""

big_list = [[['one', 'two'], ['seven', 'eight']], [['nine', 'four'], ['three', 'one']], [['two', 'eight'], ['seven', 'four']], [['five', 'one'], ['four', 'two']], [['six', 'eight'], ['two', 'seven']], [['three', 'five'], ['one', 'six']], [['nine', 'eight'], ['five', 'four']], [['six', 'three'], ['four', 'seven']]]

word_counts = {}

for lst in big_list:
    for lst2 in lst:
        for word in lst2:
            if word not in word_counts:
                word_counts[word] = 0
                
            word_counts[word] += 1
            
print(word_counts)
                