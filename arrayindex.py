# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:04:38 2019

@author: Siva
"""
#Given a number N and an array of N elements ,print each element with its index
n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    print(arr[i],i)
