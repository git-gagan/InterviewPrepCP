#Sort the array, then iterate and see the count.
def toyCount(N, K, arr):
    arr.sort()
    i = 0
    count = 0
    while i < N:
        if arr[i] <= K:
            K -= arr[i]
            count += 1
        i += 1
    return count
