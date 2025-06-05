def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            j = largest
            while 2 * j + 1 < n:
                left = 2 * j + 1
                right = 2 * j + 2
                largest = j
                if left < n and arr[left] > arr[largest]:
                    largest = left
                if right < n and arr[right] > arr[largest]:
                    largest = right
                if largest != j:
                    arr[j], arr[largest] = arr[largest], arr[j]
                    j = largest
                else:
                    break
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        j = 0
        while 2 * j + 1 < i:
            left = 2 * j + 1
            right = 2 * j + 2
            largest = j
            if left < i and arr[left] > arr[largest]:
                largest = left
            if right < i and arr[right] > arr[largest]:
                largest = right
            if largest != j:
                arr[j], arr[largest] = arr[largest], arr[j]
                j = largest
            else:
                break
    return arr