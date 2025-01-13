"""
두 개의 문자열 str1과 str2가 주어진다.
문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오
존재하면 1, 존재하지 않으면 0
"""

def find_pattern_to_kmp(pattern, text):
    def set_kmp_table():
        length = len(pattern)
        table = [0 for _ in range(length)]

        pattern_index = 0
        for idx in range(1, length):
            # pattern_index가 0이 되거나, pattern_index 글자와 idx번 글자가 같아질 때까지
            while pattern_index > 0 and pattern[pattern_index] != pattern[idx]:
                pattern_index = table[pattern_index - 1]

            if pattern[idx] == pattern[pattern_index]:
                pattern_index += 1
                table[idx] = pattern_index

        return table

    pattern_table = set_kmp_table()

    # 결과를 만족하는 인덱스 시점
    result = []
    p_idx = 0

    for idx in range(len(text)):
        # 패턴과 달라지게 된다면, 그 시점부터 다시 시작
        while p_idx > 0 and text[idx] != pattern[p_idx]:
            p_idx = pattern_table[p_idx - 1]

        if text[idx] == pattern[p_idx]:
            # 패턴의 끝까지 진행했다면(일치한다면) 저장
            if p_idx == len(pattern) - 1:
                result.append(idx - len(pattern)+1)
                p_idx = pattern_table[p_idx]
            else:
                p_idx += 1

    return result

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    idx_list = find_pattern_to_kmp(str1, str2)
    answer = 1 if len(idx_list) != 0 else 0
    print(f"#{tc} {answer}")

