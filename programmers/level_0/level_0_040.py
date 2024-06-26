"""
부분 문자열인지 확인하기

부분 문자열이란 문자열에서 연속된 일부분에 해당하는 문자열을 의미합니다.
예를 들어, 문자열 "ana", "ban", "anana", "banana", "n"는 모두 문자열 "banana"의 부분 문자열이지만,
"aaa", "bnana", "wxyz"는 모두 "banana"의 부분 문자열이 아닙니다.

문자열 my_string과 target이 매개변수로 주어질 때, target이 문자열 my_string의 부분 문자열이라면 1을,
아니라면 0을 return 하는 solution 함수를 작성해 주세요.

1 ≤ my_string의 길이 ≤ 100
my_string은 영소문자로만 이루어져 있습니다.
1 ≤ target의 길이 ≤ 100
target은 영소문자로만 이루어져 있습니다.
"""
from utils import prvalue


@prvalue()
def solution(my_string: str, target: str) -> int:
    return 1 if target in my_string else 0


@prvalue()
def solution001(my_string: str, target: str) -> int:
    return int(target in my_string)


@prvalue()
def solution002():
    pass


if __name__ == '__main__':
    assert solution("banana", "ana") == 1
    assert solution("banana", "ban") == 1
    assert solution("banana", "anana") == 1
    assert solution("banana", "banana") == 1
    assert solution("banana", "wxyz") == 0
    assert solution("banana", "aaa") == 0
    assert solution("banana", "bnana") == 0
