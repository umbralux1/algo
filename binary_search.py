

def binary_search(item: int, arr: list[int]) -> int | None:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


test_list = [1, 3, 5, 7, 9]

res1 = binary_search(3, test_list)
print(res1)
assert res1 == 1


res2 = binary_search(-1, test_list)
print(res2)
assert res2 is None

res3 = binary_search(10, test_list)
print(res3)
assert res3 is None

res4 = binary_search(7, test_list)
print(res4)
assert res4 == 3
