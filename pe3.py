#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:47:47 2019

Find the largest prime factor of 600851475143
or find the inverse of the smallest prime factor of 600851475143 in the range of 600851475143

@author: Achint the BIG DAWG!!
"""
n = 600851475143
l = 0 
for i in range(2,n):
    if (n % i == 0):
        l = n / i 
        break;

print(l)
#8462696833.0