"""
A, B에게 교과서에서 찾을 페이지 번호를 알려주면
이진 탐색으로 페이지를 먼저 펼치는 사람이 이김

이긴 사람을 출력, 비겼다면 0 출력
"""

def binary_search(total_page, find_page):
    cnt = 0
    start, end = 1, total_page

    while start <= end:
        cnt += 1
        mid = (start + end) // 2

        if mid == find_page:
            return cnt

        elif mid > find_page:
            end = mid

        else:
            start = mid

    return cnt

# TC 개수
T = int(input())

for tc in range(1, T+1):
    # 전체 수, A의 페이지, B의 페이지
    P, A, B = map(int, input().split())
    count_A, count_B = binary_search(P, A), binary_search(P, B)

    result = "A" if count_A < count_B else "B" if count_B < count_A else "0"
    print(f"#{tc} {result}")


