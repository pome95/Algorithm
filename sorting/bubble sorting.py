#!/usr/bin/env python
# coding: utf-8

import random

def bubblesort(data):
  for index in range(len(data) -1):
    swap = Flase
    for index2 in range(len(data) - index -1):
      if data[index2] > data[index2 +1]:
        data[index2], data[index2 +1] = data[index2 +1], data[index2]
        swap = True
        
  if swap == False:
    break
return data

data_list = random.sample(range(100),50)
print(data_list)
print(bubblesort(data_list))

# Result => [64, 56, 98, 97, 75, 52, 59, 10, 17, 92, 66, 47, 86, 46, 96, 48, 
# 61, 21, 74, 65, 8, 53, 16, 94, 76, 50, 54, 6, 31, 45, 38, 84, 91, 7, 
# 13, 26, 28, 62, 20, 77, 39, 22, 34, 9, 89, 40, 30, 32, 95, 3]

# [3, 6, 7, 8, 9, 10, 13, 16, 17, 20, 21, 22, 26, 28, 30, 31, 32, 34, 38, 
# 39, 40, 45, 46, 47, 48, 50, 52, 53, 54, 56, 59, 61, 62, 64, 
# 65, 66, 74, 75, 76, 77, 84, 86, 89, 91, 92, 94, 95, 96, 97, 98]
