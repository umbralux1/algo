

def find_smallest(arr: list[int]) -> int:
    smallest = 0

    for i in range(len(arr)):
        if arr[smallest] > arr[i]:
            smallest = i

    return smallest


def selection_sort(arr: list[int]) -> list[int]:
    res = []

    arr = list(arr)
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        res.append(arr.pop(smallest))

    return res


assert selection_sort([2, 3, 10, 5]) == [2, 3, 5, 10]


