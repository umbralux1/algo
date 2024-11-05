

def binary_search(item, arr: list):
    lo = 0
    hi = len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        guess = arr[mid]

        if guess == item:
            return mid
        elif guess > item:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


test_list = [1, 3, 5, 7, 9]

res1 = binary_search(3, test_list)
print(res1)
assert res1 == 1


res2 = binary_search(-1, test_list)
print(res2)
assert res2 == -1

res3 = binary_search(10, test_list)
print(res3)
assert res3 == -1

res4 = binary_search(7, test_list)
print(res4)
assert res4 == 3
