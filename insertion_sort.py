

def insertion_sort(arr: list) -> list:
    for i in range(len(arr)-1):
        while i >= 0 and arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i -= 1
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



