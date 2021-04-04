## 삽입 정렬 (Insertion Sort)
### Using python list


**삽입 정렬 기본 구현**
```python
import random

def insertion_sort(data):
    for index in range(len(data)-1):
        for stand in range(index+1, 0,-1):
            if data[stand] < data[stand -1]:
                data[stand], data[stand-1] = data[stand-1], data[stand]
            else:
                break
    return data
```

**숫자 대입후 정렬하기**
```python
data_list = random.sample(range(100),20)
data_list
insertion_sort(data_list)
```

**결과**
Result => [47, 27, 13, 74, 31, 95, 16, 64, 96, 6, 39, 42, 17, 68, 45, 20, 44, 84, 87, 56]  

[6, 13, 16, 17, 20, 27, 31, 39, 42, 44, 45, 47, 56, 64, 68, 74, 84, 87, 95, 96]  
