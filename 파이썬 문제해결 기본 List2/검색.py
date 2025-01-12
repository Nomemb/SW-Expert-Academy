"""
검색이란?

저장되어 있는 자료 중에서 원하는 항목을 찾는 작업

종류
- 순차 검색
    정렬이 안 되어 있을 경우
        시간 복잡도 O(n)

    정렬 되어 있을 경우
        검색 값이 리스트의 현재 인덱스 값보다 큰데 여태까지 없었다면,
        해당 리스트에 검색 값이 없다는 뜻.
        평균 비교 회수가 반으로 줄어들긴 함.

        그러나 시간 복잡도는 여전히 O(n)

- 이진 검색
    가운데 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속함.
    대신 자료가 반드시 정렬되어있어야 함.
    시간 복잡도는 O(logN)

- 인덱스
    테이블에 대한 동작 속도를 높임
    룩 업 테이블 등의 용어로 사용함.

    List 를 사용한 인덱스
        대량의 데이터를 매번 정렬하면, 프로그램의 반응이 느려짐.
        따라서 대량 데이터의 성능 저하 문제를 해결하기 위해 List 인덱스를 사용할 수 있음

"""

# 이진 검색
def binary_search(a, key):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if key == a[mid]:
            return mid

        elif key < a[mid]:
            end = mid - 1

        else:
            start = mid + 1

    return False

def recursive_binary_search(a, low, high, key):
    # 검색 실패
    if low > high:
        return False

    else:
        mid = (low + high) // 2
        if key == a[mid]:
            return True

        elif key < a[mid]:
            return recursive_binary_search(a, low, mid - 1, key)

        else:
            return recursive_binary_search(a, mid + 1, high, key)


# 