# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:21:02 2019

@author: Siva
"""
#Count the numbers from the given string
n=input()
c=0
if(len(n)<=1000):
    for i in n:
        if(i.isdigit()):
            c=c+1
else:
    print("invald")
print(c)
