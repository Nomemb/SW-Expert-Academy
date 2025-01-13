"""
Memoization

프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해, 매번 다시 계산하지 않도록 해
전체적인 실행 속도를 빠르게 하는 기술

DP의 핵심.

fibonacci 등에 활용
"""

memo = [0,1]
def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]
