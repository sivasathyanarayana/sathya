# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 21:01:15 2019

@author: Siva
"""
#program to swap two numbers using bitwise operator(xor)
n=list(map(int,input().split()))
a=n[0]
b=n[1]
a=a^b
b=a^b
a=a^b
print(a,b)
