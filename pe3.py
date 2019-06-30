#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:47:47 2019

Find the largest prime factor of 600851475143

The code works for any generic n, for powers of 2, the n is reduced to 1 
hence the largest prime factor would is equal to  2 
 

@author: Achint the BIG DAWG!!
"""



n = 600851475143
i = 2

while i * i <= n:
    while n % i == 0:
        n = n / i
    i = i + 1

if n == 1:
    n = 2
print(n)

#6857

