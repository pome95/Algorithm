## 병합 정렬 (Merge Sort)
### Using python list


**병합 정렬 기본 구현**

**합치기 함수**
```python
import random

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0
    
    # case1 - left/right 둘다 있을때
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged.append(right[right_point])
            right_point += 1
        else:
            merged.append(left[left_point])
            left_point += 1

    # case2 - left 데이터가 없을 때
    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1
        
    # case3 - right 데이터가 없을 때
    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1
    
    return merged
```

**나누기 함수**
```python
def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    return merge(left, right)
```

**숫자 대입후 정렬하기**
```python
data_list = random.sample(range(100), 10)
data_list
mergesplit(data_list)
```

**결과**
Result => [74, 6, 33, 53, 55, 56, 59, 49, 85, 12]  

[6, 12, 33, 49, 53, 55, 56, 59, 74, 85]  
 
