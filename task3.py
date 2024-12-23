import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

if __name__ == '__main__':
    size = 100000
    arr = [random.randint(-1000000, 1000000) for _ in range(size)]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)