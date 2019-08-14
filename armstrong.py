# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:29:05 2019

@author: Siva
"""
#armstrong number
n=input()
sum=0
l=len(n)
n=int(n)
t=n
while(n>0):
    rem=n%10
    sum=sum+(rem**l)
    n=n//10
if(sum==t):
    print("yes")
else:
    print("no")
