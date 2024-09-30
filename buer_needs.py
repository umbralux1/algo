
def calculate_misery(goods: list[int], buyer_needs: list[int]) -> int:
    goods.sort()
    user_miseries = 0

    for bn in buyer_needs:
        user_miseries += abs(bn - goods[binary_search(bn, goods)])

    return user_miseries


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


# Пример
# # Пример
# # ввод
# goods = [8, 3, 5]
# buyerNeeds = [5, 6]
# # вывод
# res = 1 # первый покупатель покупает товар 5 и его неудовлетворённость = 0, второй также покупает товар 5 и его неудовлетворённость = 6-5 = 1

goods_1 = [8, 3, 5]
buyerNeeds_1 = [5, 6]

goods_2 = [8, 3, 12, 1]
buyerNeeds_2 = [2, 14]


print(calculate_misery(goods_1, buyerNeeds_1) == 1)
print(calculate_misery(goods_2, buyerNeeds_2) == 3)
