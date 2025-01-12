"""
셀렉션 알고리즘
    저장되어 있는 자료로부터 k번째로 크거나 작은 원소를 찾는 방법

    선택 정렬
        주어진 List 중에서 최소값을 찾음
        그 값을 List의 맨 앞에 위치한 값과 교환
        맨 처음 위치를 제외한 나머지 List를 대상으로 위의 과정을 반복
        시간 복잡도 O(n^2)

    버블 정렬
        첫 번째 자료와 두 번째 자료를, 두 번째 자료와 세 번째 자료를....끝까지 비교하면서 교환.
        시간 복잡도 O(n^2)

    카운팅 정렬
        리스트를 순회하며 각 값이 나올 때마다 해당 값을 인덱스로 하는 배열의 값을 증가.
        이후 카운팅 리스트를 누적합을 계산해 주면 해당 인덱스의 시작 위치가 나옴.
        이를 바탕으로 리스트를 정렬

        시간 복잡도 O(n+k)
        단, n이 비교적 작을 때만 가능. (메모리 낭비)
"""
a = [7,4,5,1,3]

# 선택 정렬
def selection_sort(a):
    temp = a[:]
    for i in range(0, len(temp)-1):
        minimum = i
        for j in range(i + 1, len(temp)):
            if temp[minimum] > temp[j]:
                minimum = j

        temp[i], temp[minimum] = temp[minimum], temp[i]

    print(temp)


# 버블 정렬
def bubble_sort(a):
    temp = a[:]
    length = len(temp) - 1
    for i in range(length):
        for j in range(length - i):
            if temp[j] > temp[j+1]:
                temp[j], temp[j+1] = temp[j+1], temp[j]

    print(temp)


def counting_sort(a):
    temp = [0] * len(a)
    max_value = max(a)
    count_list = [0] * (max_value+1)

    for value in a:
        count_list[value] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]

    for i in range(len(a)-1, -1, -1):
        value = a[i]
        count_list[value] -= 1
        temp[count_list[value]] = value

    print(temp)

selection_sort(a)
bubble_sort(a)
counting_sort(a)
