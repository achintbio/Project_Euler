#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:18:36 2019

@author: User
"""

import os 
import pandas as pd


a = set(range(3,1000,3))
b = set(range(5,1000,5))
c = a.union(b)
print(sum(c))