"""
str1에 포함된 글자들이 str2에 몇 개씩 들어있는 지 찾고
가장 많은 글자의 개수를 출력하는 프로그램
ex) str1 = abca, str2 = ababca인 경우
str1의 a가 str2에 3개 있으므로 가장 많은 문자가 되고 3을 출력.
"""
from collections import Counter
T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    counter1 = Counter(str1)
    counter2 = Counter(str2)

    for k, v in counter2.most_common():
        if k in counter1:
            print(f"#{tc} {v}")
            break
