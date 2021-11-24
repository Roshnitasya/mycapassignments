# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 21:02:59 2021

@author: HP
"""

x = 45
if x >= 0:
    if x == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")
    
    
    
def none():
    print(none())
    
    
def plua(a,b,c):
    print(a+b+c)
    
    add(3,5,7)
    
def minus(a,b,c,d):
    print(a-b-c-d)
    
    
    subtract(7,8,9,10)
    

def add(num_1,num_2):
    print (num_1+num_2)
    
def subtract(num_1 ,num_2):
    print(num_1-num_2)


print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n")
   
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
  
if select == 1:
    print(num_1, "+", num_2, "=",
                    add(num_1, num_2))
  
elif select == 2:
    print(num_1, "-", num_2, "=",
                    subtract(number_1, number_2))
  