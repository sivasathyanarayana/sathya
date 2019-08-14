# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:33:40 2019

@author: Siva
"""

#check whether number is prime or not
def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return "no"
            break
    return "yes"
n1=int(input())
print(prime(n1))
