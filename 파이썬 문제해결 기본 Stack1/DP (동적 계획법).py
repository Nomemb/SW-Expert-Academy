"""
Dynamic Programming 의 약자

Greedy와 같이 최적화 문제를 해결하는 알고리즘

크기가 작은 부분문제를 먼저 구하고, 확대함.

구현 방식
- recursive
    overhead 발생할 수 있음
- iterative
    반복적 구조로 구현한 것이 성능면에서 효율적
"""

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]

