# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:24:46 2019

@author: Siva
"""
#check whether the number is palindrome or not
def palindrome(m):
    rev=0
    rem=0
    while(m>0):
        rem=m%10
        rev=rev*10+rem
        m=m//10
    return rev
n=int(input())
r=palindrome(n)
if(r==n):
    print("yes")
else:
    print("no")
