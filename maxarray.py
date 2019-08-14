# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:24:41 2019

@author: Siva
"""
#The given number N and an array of N integers , print the maximum element
n=int(input())
lis=list(map(int,input().split()))
max=lis[0]
for i in lis:
    if(max<i):
        max=i
print(max)
