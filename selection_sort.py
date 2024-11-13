

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


def in_place_selection_sort(arr: list) -> list:
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([2]))
assert selection_sort([2]) == [2]
assert in_place_selection_sort([2]) == [2]


print(in_place_selection_sort([2, 3]))
assert selection_sort([2, 3]) == [2, 3]
assert in_place_selection_sort([2, 3]) == [2, 3]


print(in_place_selection_sort([2, 3, 10, 5]))
assert selection_sort([2, 3, 10, 5]) == [2, 3, 5, 10]
assert in_place_selection_sort([2, 3, 10, 5]) == [2, 3, 5, 10]


