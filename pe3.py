#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:47:47 2019

@author: User
"""

l = 0 
for i in range(2,600851475143):
    if (600851475143 % i == 0):
        l = 600851475143 / i 
        break;

print(l)