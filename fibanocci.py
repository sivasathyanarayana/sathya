# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:22:55 2019

@author: Siva
"""
#given number N find print fibanocci series of N numbers
n=int(input())
a=0
b=1;print(b,end=" ")
for i in range(n-1):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    
