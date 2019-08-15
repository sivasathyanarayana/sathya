# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:21:02 2019

@author: Siva
"""
#Count the lines from the given paragraph
n=input()
c=1
if(len(n)<=1000):
    for i in n:
        if(i=="."):
            c=c+1
else:
    print("invald")
print(c)
