## 선택 정렬 (Selection) Sort)
### Using python list


**선택 정렬 기본 구현**
```python
import random

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data
```

**숫자 대입후 정렬하기**
```python
data_list = random.sample(range(100),20)
data_list
selection_sort(data_list)
```

**결과**
Result => [39, 43, 63, 10, 97, 24, 96, 64, 59, 65, 93, 82, 44, 84, 0, 53, 88, 33, 98, 80]  

[0, 10, 24, 33, 39, 43, 44, 53, 59, 63, 64, 65, 80, 82, 84, 88, 93, 96, 97, 98] 
