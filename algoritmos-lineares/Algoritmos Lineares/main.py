import _generate_randoms
import _quick_sort
import _merge_sort
import _heap_sort
import _counting_sort
import _radix_sort
import _bucket_sort

for i in range(1, 1000):
    random_numbers = _generate_randoms.generate_randoms(i)
    for j in range(1, 20):
        quick_sorted = _quick_sort.quick_sort(random_numbers)
    for j in range(1, 20):
        merge_sorted = _merge_sort.merge_sort(random_numbers)
    for j in range(1, 20):
        heap_sorted = _heap_sort.heap_sort(random_numbers)
    for j in range(1, 20):
        counting_sorted = _counting_sort.counting_sort(random_numbers)
    for j in range(1, 20):
        radix_sorted = _radix_sort.radix_sort(random_numbers)
    for j in range(1, 20):
        bucket_sorted = _bucket_sort.bucket_sort(random_numbers)
    