# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 12:35:18 2021

@author: Roshni Tasya 
"""

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
        
fib(18)