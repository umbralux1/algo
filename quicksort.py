

def quicksort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]

    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([1, 2]))
assert quicksort([1, 2]) == [1, 2]

assert quicksort([2, 5, 10, 3, 6]) == [2, 3, 5, 6, 10]

print(quicksort([1, 1, 1]))
assert quicksort([1, 1, 1]) == [1, 1, 1]

assert quicksort([5, 4, 3, 3, 2, 1]) == [1, 2, 3, 3, 4, 5]


assert quicksort([]) == []

assert quicksort([1]) == [1]
