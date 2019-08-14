# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:05:30 2019

@author: Siva
"""
#print even numbers between 2 numbers(interval)
lis=list(map(int,input().split()))
n=lis[0]
q=lis[1]
for i in range(n+1,q):
    if(i%2==0):
        print(i,end=" ")

