"""가운데 글자 가져오기
단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

재한사항
- s는 길이가 1 이상, 100이하인 스트링입니다.

입출력
- abcde   c
- qwer    we
"""


def solution(s: str):
    length = len(s) // 2
    if len(s) % 2 != 0:
        return s[length:length + 1]
    return s[length - 1:length + 1]


if __name__ == '__main__':
    assert solution('abcde') == 'c'
    assert solution('qwer') == 'we'
