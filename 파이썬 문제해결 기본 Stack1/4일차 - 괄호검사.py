"""
주어진 입력에서 {, }, (, )가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오
"""

T = int(input())

for tc in range(1, T + 1):
    input_str = input()

    stack = []
    is_pair = True
    for s in input_str:
        if s == '(' or s == '{':
            stack.append(s)

        elif s == '}':
            if len(stack) == 0 or stack[-1] != '{':
                is_pair = False
                break

            else:
                stack.pop()

        elif s == ')':
            if len(stack) == 0 or stack[-1] != '(':
                is_pair = False
                break

            else:
                stack.pop()

    print(f"#{tc} 0" if not is_pair or stack else f"#{tc} 1")
