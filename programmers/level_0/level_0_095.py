"""
외계행성의 나이

우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다.
입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다.
a는 0, b는 1, c는 2, ..., j는 9입니다.
예를 들어 23살은 cd, 51살은 fb로 표현합니다.
나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

age는 자연수입니다.
age ≤ 1,000
PROGRAMMERS-962 행성은 알파벳 소문자만 사용합니다.

23	"cd"
51	"fb"
100	"baa"
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(age: int):
    age_map = {str(i): chr(ord("a") + i) for i in range(10)}
    return "".join([age_map[k] for k in str(age)])


@prvalue(print_result=True)
def solution001(age: int):
    return "".join([chr(int(x) + 97) for x in str(age)])


if __name__ == '__main__':
    assert solution(23) == "cd"
    assert solution(51) == "fb"
    assert solution(100) == "baa"
    assert solution001(23) == "cd"
    assert solution001(51) == "fb"
    assert solution001(100) == "baa"
