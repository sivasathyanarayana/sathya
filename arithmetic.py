# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 00:07:59 2019

@author: Siva
"""
#find the sum of arithmetic progression till N terms given n,a,d 
lis=list(map(int,input().split()))
n=lis[0]
a=lis[1]
d=lis[2]
sum=(n/2)*(2*a+((n-1)*d))
print((int(sum)))
