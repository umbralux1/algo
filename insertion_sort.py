

def insertion_sort(arr: list):
    for i in range(len(arr) - 1):
        j = i
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1

    return arr


print(insertion_sort([1, 2]))
assert insertion_sort([1, 2]) == [1, 2]

print(insertion_sort([2, 5, 10, 3, 6]))
assert insertion_sort([2, 5, 10, 3, 6]) == [2, 3, 5, 6, 10]


print(insertion_sort([1, 1, 1]))
assert insertion_sort([1, 1, 1]) == [1, 1, 1]

print(insertion_sort([5, 4, 3, 3, 2, 1]))
assert insertion_sort([5, 4, 3, 3, 2, 1]) == [1, 2, 3, 3, 4, 5]


assert insertion_sort([]) == []

assert insertion_sort([1]) == [1]



