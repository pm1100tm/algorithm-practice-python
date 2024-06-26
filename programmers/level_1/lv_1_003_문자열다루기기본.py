"""문자열 다루기 기본

문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
s는 길이 1 이상, 길이 8 이하인 문자열입니다.

s    return
a234 false
1234 true
"""


def solution(s: str) -> bool:
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()

    return False


if __name__ == '__main__':
    assert solution('a234') is False
    assert solution('1234') is True
