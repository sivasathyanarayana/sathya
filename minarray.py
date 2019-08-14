# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:24:41 2019

@author: Siva
"""
#The given number N and an array of N integers , print the minimum element
n=int(input())
lis=list(map(int,input().split()))
min=lis[0]
for i in lis:
    if(min>i):
        min=i
print(min)
