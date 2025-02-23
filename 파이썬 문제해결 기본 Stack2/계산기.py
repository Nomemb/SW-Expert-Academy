"""
문자열로 된 계산식이 주어질 때 스택을 이용해 계산할 수 있음

일반적 방법
1. 중위표기법의 수식을 후위표기법으로 변경
    A + B --> AB +

    ex) A*B - C/D를 후위표기법으로 바꾸는 방법
    1-1. 우선순위에 따라 괄호로 묶어줌
        ( (A*B) - (C/D) )
    1-2. 후위표기법으로 변경
        ( (A B)* (C D)/ ) -
    1-3. 괄호 제거
        AB* CD/-

    단점) 프로그램으로 작성하기는 어려움. 따라서 알고리즘을 개발함.

    변환 알고리즘
    1. 입력받은 알고리즘에서 토큰을 읽음
    2. 토큰이 피연산자이면 토큰을 출력
    3. 토큰이 연산자(괄호 포함) 일 경우
        3-1. 우선순위가 높으면 스택에 push
        3-2. 우선순위가 안 높으면, 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 pop 한 후
             토큰의 연산자를 push
        3-3. top에 연산자가 없으면 push

    4. 토큰이 오른쪽 괄호일 경우
        4-1. top에 왼쪽 괄호가 올 떄까지 pop 연산 수행
        4-2. pop한 연산자를 출력.
        4-3. 왼쪽 괄호를 만나면 pop만 하고 출력하지는 않음.

    5. 중위 표기식에 더 읽을 게 없다면 중지. 있다면 1부터 반복
    6. 스택에 남아 있는 연산자를 모두 pop 해 출력
        스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음

2. 변경 이후 계산법
    1. 피연산자를 만나면 스택에 push
    2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop해 연산, 연산결과를 다시 스택에 push
    3. 수식이 끝나면 마지막으로 스택을 pop해 출력
"""

example = "(6+5*(2-8)/2)"
expect = "6528-*2/+"

# isp: In Stack Priority
operation_dict = {
    ')':{
        "ISP":None, "ICP":None
    },
    '*':{
        "ISP":2, "ICP":2
    },
    '/': {
        "ISP":2, "ICP":2
    },
    '+': {
        "ISP":1, "ICP":1
    },
    '-': {
        "ISP":1, "ICP":1
    },
    '(': {
        "ISP":0, "ICP":3
    }
}


def convert_infix_to_postfix(infix_str):
    stack = []
    postfix_list = []
    for s in infix_str:
        if s.isalnum():
            postfix_list.append(s)

        else:
            if s == ')':
                while stack:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        postfix_list.append(stack.pop())

            else:
                if len(stack) == 0:
                    stack.append(s)

                else:
                    # Stack 맨 위의 우선순위보다 현재 연산자의 우선순위가 높을 경우 그냥 추가
                    if operation_dict[stack[-1]]["ISP"] < operation_dict[s]["ICP"]:
                        stack.append(s)
                    else:
                        while stack:
                            # Stack 맨 위 우선순위가 현재 우선순위보다 작을때까지 pop
                            if operation_dict[stack[-1]]["ISP"] >= operation_dict[s]["ICP"]:
                                postfix_list.append(stack.pop())
                            else:
                                break
                        stack.append(s)

    while stack:
        postfix_list.append(stack.pop())

    print(''.join(postfix_list))
    return ''.join(postfix_list)

def calculate_postfix(postfix_str):
    stack = []
    for s in postfix_str:
        if s.isalnum():
            stack.append(s)
        else:
            try:
                b = int(stack.pop())
                a = int(stack.pop())

                if s == '+':
                    stack.append(a + b)
                elif s == '-':
                    stack.append(a - b)
                elif s == '*':
                    stack.append(a * b)
                elif s == '/':
                    stack.append(a / b)

            except Exception as e:
                print(e)

    return stack.pop()


convert_postfix = convert_infix_to_postfix("3+(4+5)*6+7")
print(calculate_postfix(convert_postfix))