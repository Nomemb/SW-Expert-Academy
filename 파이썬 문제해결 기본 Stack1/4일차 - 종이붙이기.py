"""
가로 세로 길이가 10 * 20, 20 * 20인 두 종류의 종이가 있음.

20 * N 크기의 직사각형을 채우는 방법에 대해 계산하는 프로그램
N은 10의 배수

예시)
30 -> 5,
50 -> 21
70 -> 85

DP(0) = 0
DP(1) = 1
DP(2) = DP(1) + 2 * DP(0) = 3
DP(3) = DP(2) + 2 * DP(1) = 5
DP(4) = DP(3) + 2 * DP(2) = 11
DP(5) = DP(4) + 2 * DP(3) = 21

1 3 5 x 21 x2 85
 2 2 8 8 32 32
 4  16  64
"""

T = int(input())

dp = [1, 1, 3, 5]
for tc in range(1, T + 1):
    N = int(input()) // 10
    while N >= len(dp):
        dp.append(dp[len(dp)-1] + 2 * dp[len(dp)-2])

    print(f"#{tc} {dp[N]}")