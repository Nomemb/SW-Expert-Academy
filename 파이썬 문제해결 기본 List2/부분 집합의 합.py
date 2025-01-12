"""
유한 개의 정수로 이루어진 집합이 있을 때
집합의 부분 집합 중에서 그 집합의 원소를
모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제

1) 완전 검색으로 풀기 위해선
집합의 모든 부분 집합을 생성한 후 각 부분 집합의 합을 계산

2) 주어진 집합의 부분 집합을 생성하는 방법을 생각
"""

# Case 1: Loop를 이용하여 확인하고, 부분집합을 생성
def make_subset_for_loop():
    bit = [0, 0, 0, 0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                for l in range(2):
                    bit[3] = l
                    print(bit)

# 원래 집합 base = [1, 2, 3, 4] 가 있었다면 각 비트 0일 때만 포함시켜서 계산하면 된다는 뜻.

# 비트 연산자
# 원소가 n개일 경우, 모든 부분 집합의 수는 1 << n
# i에서 j번째 비트가 1인지 아닌지 리턴하려면 i & (1 << j)


# Case 2: 비트 연산을 통해 부분집합을 생성
def make_subset_for_bitwise():
    arr = [3, 6, 7, 1, 5, 4]
    n = len(arr)

    # 부분 집합의 개수 만큼
    for i in range(1<<n):
        # 원소의 수만큼
        for j in range(n):
            # i의 j번째 비트가 1이면 j번째 원소를 출력
            if i & (1<<j):
                print(arr[j], end=',')
        print()


make_subset_for_loop()
make_subset_for_bitwise()
