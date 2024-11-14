import pytest


def binary_search(item, arr: list):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def test_binary_search_found():
    assert binary_search(3, [1, 2, 3, 4, 5]) == 2
    assert binary_search(1, [1, 2, 3, 4, 5]) == 0
    assert binary_search(5, [1, 2, 3, 4, 5]) == 4


def test_binary_search_not_found():
    assert binary_search(6, [1, 2, 3, 4, 5]) == -1
    assert binary_search(0, [1, 2, 3, 4, 5]) == -1
    assert binary_search(10, [1, 3, 5, 7, 9]) == -1


def test_binary_search_empty():
    assert binary_search(1, []) == -1


def test_binary_search_single_element():
    assert binary_search(1, [1]) == 0
    assert binary_search(2, [1]) == -1


def test_binary_search_duplicates():
    # In case of duplicates, binary search usually returns the index of any one instance of the item.
    assert binary_search(2, [1, 2, 2, 2, 3]) in [1, 2, 3]


