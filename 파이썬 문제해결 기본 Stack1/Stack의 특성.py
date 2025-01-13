"""
Stack: Last in First out :: LIFO
마지막에 삽입한 자료가 가장 먼저 꺼내지는 구조.

C언어: 배열
Python: List

마지막 삽입된 원소의 위치: top

* 고려해봐야 할 점
리스트의 크기를 변경하는 작업은 큰 Overhead를 발생시킴.

* 해결 방법
- 리스트 크기가 변동되지 않도록, 배열처럼 크기를 미리 정해놓고 사용하는 방법
- 동적 연결리스트를 이용해 저장소를 동적으로 할당하여 스택을 구현하는 방법
"""

# 스택 구현
stack = []

# 삽입 연산
def push(item):
    stack.append(item)

# 삭제 연산
def pop():
    if len(stack) == 0:
        print("Stack is empty")
        return

    else:
        return stack.pop(-1)
