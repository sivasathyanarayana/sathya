# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:45:06 2019

@author: Siva
"""
#display armstrong number b/w two intervals
lis=list(map(int,input().split()))
a=lis[0]
b=lis[1]
for i in range(a+1,b):
    rem=0
    sum=0
    p=i
    while(i>0):
        rem=i%10
        k=len(str(p))
        sum=sum+(rem**k)
        i=i//10
    if(sum==p):
        print(p,end=" ")
