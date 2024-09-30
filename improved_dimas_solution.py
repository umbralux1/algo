

tests = [
    {'goods': [8, 3, 5],
     'buyerNeeds': [5, 6]},
    {'goods': [8, 3, 12, 1],
     'buyerNeeds': [2, 14]},
]


def solution(goods: list, buyerNeeds: list):
    goods = sorted(goods)
    res = 0
    for need in buyerNeeds:
        res += get_diff(need, goods)
    return res


def get_diff(need: int, goods: list):
    return need - goods[binary_search(need, goods)]


def binary_search(item: int, arr: list[int]) -> int:
    low = 0
    high = len(arr) - 1
    closest = 0

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if abs(item - guess) < abs(item - arr[closest]):
            closest = mid

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return closest


for test in tests:
    print(solution(test['goods'], test['buyerNeeds']))
