# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 17:21:54 2019

@author: Siva
"""
#if the given string is numberic or not
import re
siva="^[.0-9]+$"
def string(ssn):
    if(re.search(siva,ssn)):
        return "yes"
    else:
        return "no"
ssn=input()
print(string(ssn))
