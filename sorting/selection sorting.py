#!/usr/bin/env python
# coding: utf-8

import random

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data


data_list = random.sample(range(100), 20)
print(data_list)
selection_sort(data_list)

# Result =>
# [67, 39, 82, 29, 12, 73, 88, 96, 78, 90, 38, 23, 95, 45, 32, 28, 72, 79, 8, 69]
# [8, 12, 23, 28, 29, 32, 38, 39, 45, 67, 69, 72, 73, 78, 79, 82, 88, 90, 95, 96]




