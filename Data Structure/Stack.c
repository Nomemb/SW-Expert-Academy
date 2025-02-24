#include <stdio.h>
#define MAX_N 100

int top;
int stack[MAX_N];

// 구현해야 할 함수 목록
void stackInit(void)
{
    top = 0;
}

int stackIsEmpty(void)
{
    return (top == 0);
}

int stackIsFull(void)
{
    return (top == MAX_N - 1);
}

int stackPush(int value)
{
    // 꽉 찼다면
    if (stackIsFull())
    {
        printf("Stack is full");
        return 0;
    }

    // 자리가 비었다면
    stack[top] = value;
    top++;
    return 1;
}

int stackPop(int *value)
{
    // 스택이 비었다면
    if (stackIsEmpty())
    {
        printf("Stack is empty");
        return 0;
    }

    top--;
    *value = stack[top];
    return 1;
}

int main(int argc, char* argv[])
{
    int T, N;

    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d", &N);
        stackInit();
        for (int i = 0; i < N; i++)
        {
            int value;
            scanf("%d", &value);
            stackPush(value);
        }

        printf("#%d ", test_case);

        while (!stackIsEmpty())
        {
            int value;
            if (stackPop(&value) == 1)
            {
                printf("%d ", value);
            }
        }
        printf("\n");
    }
    return 0;
}
