# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:54:08 2019

@author: Siva
"""
year=int(input())
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("no")
