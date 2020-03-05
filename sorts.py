def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)

    return arr

def insertion_sort(arr):

    for i in range(1, len(arr)):
        pointer = i
        store = arr[i]
        while pointer > 0 and arr[pointer-1] > store:
            arr[pointer] = arr[pointer-1]
            pointer -= 1
        if pointer < i:
            arr[pointer] = store

    return arr

def selection_sort(arr):

    for i in range(len(arr)):
        m = i
        for j in range(i, len(arr)):
            if arr[j] < arr[m]:
                m = j
        swap(arr, m, i)
    
    return arr

def quick_sort(arr, left, right):
    if right - left > 0:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid-1)
        quick_sort(arr, mid+1, right)
        return arr

def partition(arr, left, right):
    pivot = arr[right]
    j = left-1
    for i in range(left, right):
        if arr[i] < pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j+1], arr[right] = arr[right], arr[j+1]
    return j+1

arr = [3, 2, 1, 5, 2, 3, 6, 3, 8, 5, 4, 6]
print(insertion_sort(arr))

arr = [3, 2, 1, 5, 2, 3, 6, 3, 8, 5, 4, 6]
print(selection_sort(arr))

arr = [3, 2, 1, 5, 2, 3, 6, 3, 8, 5, 4, 6]
print(bubble_sort(arr))

arr = [3, 2, 1, 5, 2, 3, 6, 3, 8, 5, 4, 6]
print(quick_sort(arr, 0, len(arr)-1))
