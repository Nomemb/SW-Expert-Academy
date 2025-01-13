"""
패턴 매칭 알고리즘은 문자열 내에서 특정 문자열을 찾는 것

1. brute force
    본문 문자열을 처음부터 끝까지 순회하면서 패턴 내의 문자들을 일일히 비교
    최악의 경우 모든 위치에서 파악해야되므로 시간 복잡도 O(MN)

2. KMP 알고리즘
    불일치가 발생한 텍스트 문자열의 앞 부분에 어떤 문자가 있는지를 알고 있으므로,
    앞 부분에 대해 다시 비교하지 않고 매칭을 수행

    2-1. 패턴을 전처리 해 배열 next[M]을 구해서 잘못된 시작을 최소화함.
        next[M]: 불일치가 발생했을 경우 이동할 다음 위치

    2-2. 매칭이 실패했을 때 돌아갈 곳을 계산함.

    시간 복잡도 O(M + N)

3. 보이어-무어 알고리즘
    오른쪽에서 왼쪽으로 비교, 대부분의 상용 소프트웨어에서 채택함.
    패턴의 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는 경우,
    이동거리는 패턴의 길이 만큼이 됨.

    최악의 경우 시간복잡도는 O(MN)이지만 일반적으로는 O(N)보다 적음

"""
from collections import defaultdict


def find_pattern_to_brute_force(pattern, text):
    M, N = len(pattern), len(text)

    i, j = 0, 0
    while j < M and i < N:
        if text[i] != pattern[j]:
            i = i - j
            j = -1

        i = i + 1
        j = j + 1

    return i - M if j == M else -1


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


def find_pattern_to_boyer_moore(pattern, text):
    def set_skip_table():
        dict = defaultdict(int)
        p_length = len(pattern)
        for i in range(p_length-1, -1, -1):
            if pattern[i] not in dict:
                dict[pattern[i]] = p_length - i - 1
        return dict

    boyer_moore_table = set_skip_table()
    length_text = len(text)

    idx = len(pattern) - 1
    p_idx = len(pattern) - 1
    while idx < length_text:
        if text[idx] != pattern[p_idx]:
            if text[idx] not in boyer_moore_table:
                idx += len(pattern)
            else:
                idx += boyer_moore_table[text[idx]]

        else:
            while p_idx > 0 and text[idx] == pattern[p_idx]:
                p_idx -= 1
                idx -= 1

            if p_idx == 0:
                return idx


# print(find_pattern_to_brute_force("is", "This is a book~!"))
# # print(find_pattern_to_kmp("별똥같은별똥별", "별똥같은별똥같은별똥별"))
# print(find_pattern_to_kmp("is", "This is a book~!"))

print(find_pattern_to_boyer_moore("is", "This is a book~!"))
