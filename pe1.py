#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:18:36 2019

@author: Achint the BIG DAWG!!!
"""

import os 
import pandas as pd

n = 1000
a = set(range(3,n,3))
b = set(range(5,n,5))
c = a.union(b)
print(sum(c))

#233168