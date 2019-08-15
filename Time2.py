# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:08:06 2019

@author: Siva
"""
#Given time in minutes ,print it in hours and minutes\
n=list(map(int,input().split()))
n1=list(map(int,input().split()))
h1=n[0]
m1=n[1]
h2=n1[0]
m2=n1[1]
if(h1>h2):
    print(h1-h2,end=" ")
else:
    print(h2-h1,end=" ")
if(m1>m2):
    print(m1-m2,end="")
else:
    print(m2-m1,end="")
