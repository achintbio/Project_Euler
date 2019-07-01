#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 19:27:57 2019
Largest palindrome from two three digit numbers 
@author: Achint the BIG 
"""

#mylist = []

def finderouter():
    mylist = []
    for i in range(999, 101, -1):
        for j in range(i, 100, -1):
            product = str(i * j)
            if product[::-1] == product:
                mylist.append(int(product))
    return mylist

#breakpoint()
#print(finderouter())
                
print(max(finderouter()))