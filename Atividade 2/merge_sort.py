import random
import time

def generate_randoms(max):
    for i in range(1, max+1):
        random_numbers.append(random.randint(1, 10))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

numbers = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]

for n in numbers:
    random_numbers = []
    generate_randoms(n)
    init = time.time()
    merge_sort(random_numbers)
    end = time.time()
    execution_time_ms = (end - init) * 1000
    print(f"Tempo de execução para {n} números aleatórios: {execution_time_ms:.2f} ms")