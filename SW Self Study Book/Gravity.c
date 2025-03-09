/*
https://swexpertacademy.com/main/learn/course/lectureHtmlViewer.do#none
상자들이 쌓여있는 방, 방이 오른쪽으로 90도 회전해서
상자들이 중력의 영향을 받아 낙하함.
낙차가 가장 큰 상자를 구해 그 낙차를 출력하라.

첫 줄에 tc 수 T (1 <= T <= 100)

각 케이스 첫 줄에 방의 가로 길이 N (2 <= N <= 100), 방의 세로 길이 M (2 <= M <= 100)
다음 줄에 N개의 상자들이 쌓여 있는 높이 H (0 <= H <= M)
 */

#include <stdio.h>
#include <string.h>

int main()
{
    int T;
    int arr[101][101] = {0, };
    int boxTop[101] = {0, };
    int N, M;
    int H;
    int maxFallLength = 0;

    scanf_s("%d", &T);


    for (int tc = 1; tc <= T; tc++)
    {
        scanf_s("%d %d", &N, &M);
        // 초기화
        memset(arr, 0, sizeof(arr));
        memset(boxTop, 0, sizeof(boxTop));
        maxFallLength = 0;


        // 입력만큼 상자 배정
        for (int i = 1; i <= N; i++)
        {
            scanf_s("%d", &H);
            for (int j = 1; j <= H; j++)
            {
                arr[i][j] = 1;

                if (boxTop[j] == 0) boxTop[j] = i;
            }
        }

        for (int i = 1; i <= M; i++)
        {
            if (boxTop[i] != 0)
            {
                int countEmptySpace = 0;
                for (int j = boxTop[i] + 1; j <= N; j++)
                {
                    if (arr[j][i] == 0) countEmptySpace++;
                }
                if (countEmptySpace > maxFallLength) maxFallLength = countEmptySpace;
            }
        }
        printf("%d", maxFallLength);
    }

    return 0;
}
