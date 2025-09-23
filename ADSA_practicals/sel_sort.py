import random
import time
from typing import List, Tuple

def selection_sort_max(a: List[int]) -> Tuple[int, int]:
    """
    Sorts list 'a' in place by repeatedly selecting the maximum element
    and moving it to the end. Returns (comparisons, swaps).
    """
    comparisons = 0
    swaps = 0
    n = len(a)

    for end in range(n - 1, 0, -1):
        max_idx = 0
        for j in range(1, end + 1):
            comparisons += 1
            if a[j] > a[max_idx]:
                max_idx = j
        if max_idx != end:
            a[end], a[max_idx] = a[max_idx], a[end]
            swaps += 1

    return comparisons, swaps

def run_single_test(arr: List[int]) -> None:
    print("Input:", arr)
    arr_copy = arr.copy()
    t0 = time.perf_counter()
    comps, swaps = selection_sort_max(arr_copy)
    t1 = time.perf_counter()
    elapsed_ms = (t1 - t0) * 1000.0
    print("Sorted:", arr_copy)
    print(f"Comparisons: {comps}, Swaps: {swaps}, Time: {elapsed_ms:.3f} ms\n")

def batch_experiment(sizes=(5, 10, 50)):
    for n in sizes:
        arr = [random.randint(0, 1000) for _ in range(n)]
        print(f"--- n = {n} ---")
        run_single_test(arr)

if __name__ == "__main__":
    demo_arrays = [
        [64, 25, 12, 22, 11],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [7, 7, 3, 7, 2]
    ]
    for arr in demo_arrays:
        run_single_test(arr)

