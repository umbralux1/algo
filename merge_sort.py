

def mergesort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res


def test_mergesort():
    # Test case 1: Empty list
    assert mergesort([]) == []

    # Test case 2: Single element
    assert mergesort([1]) == [1]

    # Test case 3: Already sorted list
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test case 4: Reverse sorted list
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test case 5: List with repeated elements
    assert mergesort([4, 2, 4, 3, 2]) == [2, 2, 3, 4, 4]

    # Test case 6: List with negative numbers
    assert mergesort([-3, -1, -4, 2, 0]) == [-4, -3, -1, 0, 2]

    # Test case 7: Mixed positive and negative numbers
    assert mergesort([3, -2, 5, 1, -7]) == [-7, -2, 1, 3, 5]

    # Test case 8: List with duplicates
    assert mergesort([5, 1, 1, 3, 5, 2, 2]) == [1, 1, 2, 2, 3, 5, 5]

    print("All tests passed!")

# Run the tests
test_mergesort()
