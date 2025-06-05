import _generate_randoms
import _quick_sort
import _merge_sort
import _heap_sort
import _counting_sort
import _radix_sort
import _bucket_sort

from concurrent.futures import ProcessPoolExecutor

def run_sorts(i):
    random_numbers = _generate_randoms.generate_randoms(i)

    for _ in range(1, 20):
        _quick_sort.quick_sort(list(random_numbers))
        _merge_sort.merge_sort(list(random_numbers))
        _heap_sort.heap_sort(list(random_numbers))
        _counting_sort.counting_sort(list(random_numbers))
        _radix_sort.radix_sort(list(random_numbers))
        _bucket_sort.bucket_sort(list(random_numbers))
    return i  # Apenas para saber qual i foi processado

if __name__ == '__main__':
    import time
    start = time.time()

    with ProcessPoolExecutor() as executor:
        results = list(executor.map(run_sorts, range(1, 10)))

    print("Concluído para todos os tamanhos de entrada.")
    print(f'Tempo total: {time.time() - start:.2f} segundo(s)')