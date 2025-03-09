"""
N * N 배열에 숫자가 들어있다.
한 줄에서 하나씩 숫자를 골라 합이 최소가 되도록 하려 한다.
단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
"""
def backtracking(total, cnt):
    global total_sum
    if cnt == N:
        if total_sum > total:
            total_sum = total

    if total_sum < total:
        return

    for v in range(len(visited)):
        if not visited[v]:
            visited[v] = True
            backtracking(total + board[cnt][v], cnt + 1)
            visited[v] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    total_sum = 100

    board = []
    visited = [False for _ in range(N)]

    for i in range(N):
        board.append(list(map(int,input().split())))

    backtracking(0, 0)
    print(f"#{tc} {total_sum}")
