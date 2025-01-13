"""
ABBA같은 문자열을 회문이라고 함.
N * N 글자판에서 길이가 m인 회문을 찾는 프로그램.
가로/세로 가능.
"""

def is_palindrome(x, y, length_palindrome, board):
    is_palindrome = True
    for k in range(length_palindrome//2 + 1):
        if board[x][y + k] != board[x][y + length_palindrome - k - 1]:
            is_palindrome = False
            break

    return is_palindrome

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    word_board = []
    for i in range(N):
        word_board.append(list(input()))

    # 세로 탐색
    temp = [[""] * N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            temp[a][b] = word_board[N - b - 1][a]

    palindrome = ""
    # 가로 탐색
    i, j = 0, 0
    while len(palindrome) == 0 and i < N:
        # 범위 밖이면
        if j + M > N:
            i, j = i + 1, 0

        if is_palindrome(i, j, M, word_board):
            palindrome = "".join(word_board[i][j:j+M])

        if is_palindrome(i, j, M, temp):
            palindrome = "".join(temp[i][j:j+M])
        j += 1

    print(f"#{tc} {palindrome}")