# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:54:08 2019

@author: Siva
"""
#Sorting of an array size N from the given input
def sorting(n,arr):
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                t=arr[i]
                arr[i]=arr[j]
                arr[j]=t
    return arr
n=int(input())    
arr=list(map(int,input().split()))
print(*(sorting(n,arr)))
