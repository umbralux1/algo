

def min_arr_item(arr):
    min_item = 0
    for i in range(1, len(arr)):
        if arr[min_item] > arr[i]:
            min_item = i

    return min_item


def selection_sort(arr: list) -> list:
    res = []

    for i in range(len(list(arr))):
        min_item = min_arr_item(arr)
        res.append(arr.pop(min_item))

    return res


print(selection_sort([2]))
assert selection_sort([2]) == [2]


print(selection_sort([2, 3]))
assert selection_sort([2, 3]) == [2, 3]


print(selection_sort([2, 3, 10, 5]))
assert selection_sort([2, 3, 10, 5]) == [2, 3, 5, 10]


