#!/usr/bin/env python
# coding: utf-8

import random
data = random.sample(range(20),7)

def qsort(data):
    if len(data) <=1:
        return data
    
    left,right = list(), list()
    pivot = data[0]
    
    for index in range(1,len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])
            
    return qsort(left) + [pivot] + qsort(right)


data
qsort(data)

# Result => 
# [14, 15, 2, 8, 19, 3, 11]
# [2, 3, 8, 11, 14, 15, 19]