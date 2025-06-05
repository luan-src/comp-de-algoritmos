def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    bucket_count = 10
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = (max_val - min_val) / bucket_count + 1e-9
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)
    for i in range(bucket_count):
        buckets[i].sort()
    return [item for sublist in buckets for item in sublist]
