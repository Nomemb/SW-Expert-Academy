"""
전체를 두 개의 그룹으로 나누고, 승자끼리 카드를 비교해 이긴 사람이 최종 승자
i번부터 j번까지 속한 그룹은
i ~ (i+j)//2  ,  (i+j)//2 + 1 ~ j
로 나눔
1: 가위, 2: 바위, 3: 보
같은 카드일 경우 번호가 작은 쪽을 승자로 함.
"""


def compare_card(group):
    if len(group) == 1:
        return group[0]

    if len(group) == 2:
        if group[0][0] == group[1][0]:
            return group[0]

        if abs(group[0][0] - group[1][0]) == 1:
            return group[1] if group[0][0] - group[1][0] < 0 else group[0]

        elif abs(group[0][0] - group[1][0]) == 2:
            return group[0] if group[0][0] - group[1][0] < 0 else group[1]

    else:
        group_length = (1 + len(group)) // 2
        return compare_card([compare_card(group[:group_length]), compare_card(group[group_length:])])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    students = list(map(int, input().split()))
    tournament = []
    for i, students in enumerate(students):
        tournament.append((students, i + 1))

    print(f"#{tc} {compare_card(tournament)[1]}")