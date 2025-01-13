"""
문자열 s에서 반복문자를 지우려 한다.
지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 반복문자가 또 생기면 이부분도 지운다.

반복문자를 지운 후 남은 문자열의 길이를 출력하시오
없으면 0 출력.

"""

T = int(input())

for tc in range(1, T + 1):
    input_string = input()

    stack = []
    for s in input_string:
        if len(stack) == 0:
            stack.append(s)

        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

    print(f"#{tc} {len(stack)}")