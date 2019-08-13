# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:09:23 2019

@author: Siva
"""
lis=list(map(int,input().split()))
ll=list(map(int,input().split()))
n=lis[0]
k=lis[1]
sum=0
for i in range(0,k):
    sum=sum+ll[i]
print(sum)
