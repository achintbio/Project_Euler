#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 17:06:24 2019

@author: Achint the BIG DAWG!
"""

import numpy as np

a = list() # Create an empty list
a.append(1) # Append the list to add the first element 
a.append(2) # Append the list to add the second element
sig  = 2    # Sig is the variable that contains the sums of all even valued elemtns

# Ranging the for loop from 2,4000000 for good measure. 
#The break statement ensures that the loop is quit as soon as a value exceed 4 Milli

for i in range(2,4000000):
    a.append(a[i-1] + a[i-2])
    if(a[i] >= 4000000):
        break
    if((a[i] % 2) == 0):
        sig = sig + a[i]

print(sig)
#4613732 is the answer I got and it is the correct one as well
        
    
    
    
