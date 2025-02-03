/*
다익스트라 알고리즘
어떤 변도 음수 가중치를 갖지 않을때 출발점과 도착점 사이의
최단 경로 문제를 푸는 알고리즘

예시문제::
방향이 있는 그래프에서 꼭지점들을 연결하는 비용이 할당 되었을 때,
임의의 꼭지점에서 다른 꼭지점으로 가는 경로들 중 비용이 가장 적게 드는 경로
즉, 두 정점 사이의 최단 경로를 찾아라.

입력예시::
첫 번쨰 라인: 전체 테스트케이스 개수
두 번째 라인: 정점 개수, 시작 정점, 도착 정점(정점의 최대 개수 100)
세 번째 라인: 정점을 잇는 간선 개수(m)

네 번째 라인~: 연결 된 정점 값 2개와 간선에 할당 된 비용이 m번 들어옴.
간선 방향==> 첫번째입력 정점 ==> 두번째 입력 정점
 */

#include <stdio.h>

#define N 100
#define INF 100000

int map[N + 1][N + 1];  // 최대 가능 크기보다 크게 설정
int visited[N + 1];     // 방문 판별 배열
int dist[N + 1];        // 거리 갱신 배열
int vertex;             // 정점
int edge;               // 정점 사이 관계
int start;
int end;

void dijkstra()
{
    int i;
    int j;
    int min;
    int v;

    dist[start] = 0;

    for (i = 1; i <= vertex; i++)
    {
        min = INF;

        for (j = 1; j <= vertex; j++)
        {
            // 방문하지 않았고, 현재 최소 거리보다 해당 거리가 짧다면 갱신
            if (visited[j] == 0 && dist[j] < min)
            {
                min = dist[j];
                v = j;
            }
        }

        visited[v] = 1;

        for (j = 1; j <= vertex; j++)
        {
            // 다음 간선까지 직통 거리보다 경유 시 짧은 루트가 있다면 해당 거리로 갱신
            if (dist[j] > dist[v] + map[v][j])
            {
                dist[j] = dist[v] + map[v][j];
            }
        }
    }
}

int main(void)
{
    int test_case;
    int T;
    int i;
    int j;
    int from;
    int to;
    int value;

    scanf("%d", &T);
    for (test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d %d %d", &vertex, &start, &end);  // 정점 개수, 시작 정점, 도착 정점 입력 받아옴
        scanf("%d", &edge);                        // 간선 개수 받아옴

        // 받은 정점 개수까지 각 길이를 INF로 초기화
        for (i = 1; i <= vertex; i++)
        {
            for (j = 1; j <= vertex; j++)
            {
                if (i != j)
                {
                    map[i][j] = INF;
                }
            }
        }

        // 간선 수만큼 반복하며 정보 갱신
        for (i = 1; i <= edge; i++)
        {
            scanf("%d %d %d", &from, &to, &value);
            map[from][to] = value;
        }

        // 각 정점의 최단거리를 INF값으로 초기화
        for (i = 1; i <= vertex; i++)
        {
            dist[i] = INF;
            visited[i] = 0;
        }

        dijkstra();
        printf("#%d %d\n", test_case, dist[end]);
    }
    return 0;
}