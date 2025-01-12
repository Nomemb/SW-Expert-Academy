"""
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
집합 A의 부분 집합 중 N개의 원소를 갖고 있고,
원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.

예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
"""

# TC 개수
T = int(input())
A = [i for i in range(1, 13)]
for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    length = len(A)

    for i in range(1 << length):
        temp = []
        for j in range(length):
            if i & (1 << j):
                temp.append(A[j])

        if len(temp) == N and sum(temp) == K:
            cnt += 1

    print(f"#{tc} {cnt}")
