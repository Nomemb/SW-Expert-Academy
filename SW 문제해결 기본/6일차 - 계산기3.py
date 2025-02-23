# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&problemLevel=5&contestProbId=AV14tDX6AFgCFAYD&categoryId=AV14tDX6AFgCFAYD&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=ALL&select-1=5&pageSize=10&pageIndex=1
from collections import deque

tc_cnt = 10

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

for tc in range(1, tc_cnt + 1):
    str_len = int(input())
    data = input()

    oper_stack = []
    postfix_list = []

    for s in data:
        if s.isalnum():
            postfix_list.append(s)

        else:
            if s == ')':
                while oper_stack:
                    if oper_stack[-1] == '(':
                        oper_stack.pop()
                        break
                    else:
                        postfix_list.append(oper_stack.pop())

            else:
                if len(oper_stack) == 0:
                    oper_stack.append(s)

                else:
                    if operation_dict[oper_stack[-1]]["ISP"] < operation_dict[s]["ICP"]:
                        oper_stack.append(s)
                    else:
                        while oper_stack:
                            if operation_dict[oper_stack[-1]]["ISP"] >= operation_dict[s]["ICP"]:
                                postfix_list.append(oper_stack.pop())
                            else:
                                break
                        oper_stack.append(s)

    while oper_stack:
        postfix_list.append(oper_stack.pop())

    postfix = ''.join(postfix_list)
    answer = []
    for s in postfix:
        if s.isalnum():
            answer.append(s)
        else:
            try:
                b = int(answer.pop())
                a = int(answer.pop())

                if s == '+':
                    answer.append(a + b)
                elif s == '-':
                    answer.append(a - b)
                elif s == '*':
                    answer.append(a * b)
                elif s == '/':
                    answer.append(a / b)

            except Exception as e:
                print(e)

    print(f"#{tc} {answer[0]}")



