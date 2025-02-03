"""
각 변에 16진수 숫자 0-F가 적혀있다.
시계방향으로 뚜껑을 돌릴 수 있고, 돌릴 때마다 시계방향으로 한 칸씩 회전

각 변에는 동일한 개수의 숫자가 있고
시계방향 순으로 높은 자리 숫자에 해당, 하나의 수를 나타냄

ex) Fig.1은 1A3, B54, 8F9, D66이고, Fig.2는 61A, 3B5, 48F, 9D6

자물쇠 비밀번호는 보물상자 수로 만들 수 있는 모든 수 중 K번쨰로 큰 수를 10진수로 만든 수.

제약사항::
N은 4의 배수이고 8 <= N <= 28
"""

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    dq = deque()
    dq.extend(list(input()))
    length = N // 4

    num_set = set()
    for i in range(length):
        temp = ["".join(list(dq)[j * length : (j + 1) * length]) for j in range(4)]
        for t in range(len(temp)):
            t_10 = int(temp[t], 16)
            if t_10 not in num_set:
                num_set.add(t_10)

        dq.appendleft(dq.pop())

    num_set = list(num_set)
    num_set.sort(reverse=True)
    print(f"#{tc} {num_set[K-1]}")
