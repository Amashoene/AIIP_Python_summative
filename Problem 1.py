# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 09:18:42 2020

@author: 212560144
"""

x = "cluster number"
for x  in range(1,33):
    import random
    cluster = [random.random() for i in range(1,17)]
    print('cluster', x,cluster)
else:
    print("finished")    