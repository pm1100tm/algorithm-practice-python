"""의상
https://school.programmers.co.kr/tryouts/85918/challenges?language=python3
- itea
combinations(조합)
"""
import itertools
from collections import defaultdict


def solution(clothes: list[list[str]]) -> int:
    """
    Failed
    """
    clothes_map = defaultdict(list)
    for name, type_ in clothes:
        clothes_map[type_].append(name)

    answer = 0
    data_list = [v for v in clothes_map.values()]
    for i in range(len(data_list)):
        for j in range(i, len(data_list)):
            answer += len(list(itertools.product(*data_list[i:j + 1])))

    return answer


def solution2(clothes: list[list[str]]) -> int:
    clothes_dict = defaultdict(list)
    for name, type_ in clothes:
        clothes_dict[type_].append(name)

    n = 1
    for type_ in clothes_dict.keys():
        # 각 종류에서 선택할 수 있는 경우의 수는 해당 종류의 의상 수 + 1 이다.
        # 여기서 +1 은 해당 종류의 의상을 선택하지 않는 경우의 수를 포함한다
        # 예를 들어, headgear는 2개의 의상이 있으므로 선택할 수 있는 경우의 수는 2 + 1 = 3
        # 즉, ("yellow_hat", "green_turban", 선택하지 않음)
        n *= len(clothes_dict[type_]) + 1

    # 적어도 한 가지 이상의 옷을 입어야 하므로 옷을 전혀 선택하지 않는 시나리오를 고려하여 n - 1 처리
    return n - 1


if __name__ == '__main__':
    assert solution(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],
    ) == 5
    assert solution(
        [
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ],
    ) == 3

    assert solution2(
        [
            ["yellow_hat", "headgear"],
            ["blue_sunglasses", "eyewear"],
            ["green_turban", "headgear"],
        ],
    ) == 5
    assert solution2(
        [
            ["crow_mask", "face"],
            ["blue_sunglasses", "face"],
            ["smoky_makeup", "face"],
        ],
    ) == 3
