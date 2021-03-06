#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data


# In[3]:


data_list = random.sample(range(100),20)
print(data_list)
print(insertion_sort(data_list))

