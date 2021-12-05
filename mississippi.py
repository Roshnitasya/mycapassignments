# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:47:14 2021

@author: Roshni Tasya 
"""

def word(str):
    dict = {}
    for n in str:
        num = dict.keys()
        if n in num:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(word('mississippi'))

