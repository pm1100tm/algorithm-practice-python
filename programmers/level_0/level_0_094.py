"""
문자열 잘라서 정렬하기

문자열 myString이 주어집니다.
"x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을
return 하는 solution 함수를 완성해 주세요.
단, 빈 문자열은 반환할 배열에 넣지 않습니다.

1 ≤ myString ≤ 100,000
myString은 알파벳 소문자로 이루어진 문자열입니다.

"axbxcxdx"	["a","b","c","d"]
"dxccxbbbxaaaa"	["aaaa","bbb","cc","d"]
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(my_string: str):
    return sorted([char for char in my_string.split("x") if char])


if __name__ == '__main__':
    assert solution("axbxcxdx") == ["a","b","c","d"]
    assert solution("dxccxbbbxaaaa") == ["aaaa","bbb","cc","d"]
    assert solution("aaxabxaabcxdx") == ['aa', 'aabc', 'ab', 'd']
