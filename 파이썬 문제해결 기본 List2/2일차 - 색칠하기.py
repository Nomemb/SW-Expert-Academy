"""
인덱스가 있는 10  * 10 격자에 빨간색과 파란색을 칠하려 함.
N개의 영역에 대해 왼쪽위, 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때
색이 겹쳐 보라색이 된 칸 수를 구하라.
"""

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    # 칠할 영역의 개수
    N = int(input())
    purple_count = 0

    board = [[0] * 10 for _ in range(10)]
    # 왼쪽 위 모서리 인덱스, 오른쪽 아래 모서리, 색상 정보
    # color--> 1: 빨강 2: 파랑 3: 보라
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        for row in range(r1, r2+1):
            for col in range(c1, c2+1):
                if board[row][col] == 0:
                    board[row][col] = color

                # 이미 보라색이면 넘어감
                elif board[row][col] == 3:
                    continue

                elif board[row][col] != color:
                    board[row][col] = 3
                    purple_count += 1

    print(f"#{_ + 1} {purple_count}")
