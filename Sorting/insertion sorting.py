#!/usr/bin/env python
# coding: utf-8

import random

def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data

data_list = random.sample(range(100),20)
print(data_list)
print(insertion_sort(data_list))

# Result => 
# [49, 24, 12, 72, 8, 17, 37, 62, 7, 71, 82, 79, 13, 61, 90, 23, 31, 99, 19, 6]
#
# [6, 7, 8, 12, 13, 17, 19, 23, 24, 31, 37, 49, 61, 62, 71, 72, 79, 82, 90, 99]