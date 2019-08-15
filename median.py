# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:13:32 2019

@author: Siva
"""
#Find median from an array
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
if(n%2==1):
    p=n//2
    print(arr[p])
else:
    p=n//2
    q=p-1
    res=(arr[p]+arr[q])/2
    print(res)

