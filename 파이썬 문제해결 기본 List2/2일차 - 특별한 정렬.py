"""
N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로
큰 수와 작은 수를 번갈아 정렬하는 방법이다.

예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
10 1 9 2 8 3 7 4 6 5

주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
"""

# TC 개수
T = int(input())

for tc in range(1, T+1):
    # 정수의 개수
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()

    answer = [0] * 10
    for i in range(10):
        answer[i] = a[(i - 1) // 2] if i % 2 else a[-(i//2 + 1)]

    print(f"#{tc}", end=' ')
    print(*answer)
