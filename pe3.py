#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:47:47 2019

Find the largest prime factor of 600851475143
or find the inverse of the smallest prime factor of 600851475143 in the range of 600851475143

@author: Achint the BIG DAWG!!
"""

l = 0 
for i in range(2,600851475143):
    if (600851475143 % i == 0):
        l = 600851475143 / i 
        break;

print(l)
#8462696833.0