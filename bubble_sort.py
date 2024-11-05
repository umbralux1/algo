import pytest


def bubble_sort(arr: list) -> list:
    for i in range(len(arr) - 1):
        is_sorted = True
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                is_sorted = False
        if is_sorted:
            return arr

    return arr


def test_bubble_sort():
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble_sort([3, 1, 4, 2]) == [1, 2, 3, 4]
    assert bubble_sort([]) == []
    assert bubble_sort([5]) == [5]
    assert bubble_sort([2, 1, 2, 1]) == [1, 1, 2, 2]
