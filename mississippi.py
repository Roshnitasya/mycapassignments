# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:47:14 2021

@author: Roshni Tasya 
"""

myDict={"I":0,"S":0,"P":0,"M":0}
word = "MISSISSIPPI"
for i in word :
    if i=="M":
        myDict["M"] = myDict["M"]+1
    elif i=="I":
        myDict["I"] = myDict["I"]+1
    elif i=="S":
        myDict["S"] = myDict["S"]+1 
    elif i=="P":
        myDict["P"] = myDict["P"]+1
        
print(myDict)        
