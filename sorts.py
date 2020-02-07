def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

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


arr = [3, 2, 1, 5, 2, 3, 6, 3, 8, 5, 4, 6]
print(insertion_sort(arr))

arr = [3, 2, 1, 5, 2, 3, 6, 3, 8, 5, 4, 6]
print(selection_sort(arr))
