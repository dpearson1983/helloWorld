# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 10:58:38 2020

@author: dpear
"""

import math
import numpy as np
#from astropy.table import Table

print("Hello, World!")

i = 0
for i in range(0,10):
    a = math.cos(i*math.pi)
    print(a)
    i = i + 1

b = np.zeros(100)
print(b)