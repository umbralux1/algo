

def quicksort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)


assert quicksort([1, 2]) == [1, 2]

assert quicksort([2, 5, 10, 3, 6]) == [2, 3, 5, 6, 10]

