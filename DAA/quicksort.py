import random
import time

def quicksort(arr, lo, hi, randomized=False):
    if lo < hi:
        if randomized:
            pi = partition_randomized(arr, lo, hi)
        else:
            pi = partition_deterministic(arr, lo, hi)
        quicksort(arr, lo, pi - 1, randomized)
        quicksort(arr, pi + 1, hi, randomized)

def partition_deterministic(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

def partition_randomized(arr, lo, hi):
    rand_idx = random.randint(lo, hi)
    arr[hi], arr[rand_idx] = arr[rand_idx], arr[hi]
    return partition_deterministic(arr, lo, hi)

def analyze_sorting_performance(sort_func, arr):
    start_time = time.time()
    sort_func(arr, 0, len(arr) - 1)
    return time.time() - start_time

if __name__ == "__main__":
    array_size = 10000
    test_array = [random.randint(0, 10000) for _ in range(array_size)]

    # Analyze deterministic quicksort
    det_array = test_array.copy()
    time_deterministic = analyze_sorting_performance(lambda arr, lo, hi: quicksort(arr, lo, hi, False), det_array)
    print(f"Deterministic Quick Sort took {time_deterministic:.5f} seconds")

    # Analyze randomized quicksort
    rand_array = test_array.copy()
    time_randomized = analyze_sorting_performance(lambda arr, lo, hi: quicksort(arr, lo, hi, True), rand_array)
    print(f"Randomized Quick Sort took {time_randomized:.5f} seconds")