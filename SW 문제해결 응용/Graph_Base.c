/*
V와 E, 정점 정보 쿼리 갯수가 주어지고
둘째 줄부터 간선의 정보가 주어짐
다음 줄에는 정점의 인접정점들이 무엇인지 묻는 쿼리가 정점 번호로 주어짐
정점 번호는 0~V-1까지. 간선정보는 오름차순으로 나열되어 주어짐.
중복 간선은 존재하지 않음.

출력::
입력으로 주어지는 쿼리 정점에 인접한 정점들을 각 줄에 출력.

입력범위::
2 <= V <= 100, 1 <= E <= 1000
*/

#include <stdio.h>
#include <malloc.h>

// 그래프의 각 정점 나타내는 구조체
typedef struct adjlistNode
{
    int vertex;                 // 번호
    struct adjlistNode *next;   // 다음 인접 정점 포인터
} AdjlistNode;

// 각 정점의 인접 리스트 나타내는 구조체
typedef struct
{
    int num_members;            // 인접 정점 수
    AdjlistNode *head;          // 인접 리스트의 첫번째 노드
    AdjlistNode *tail;          // 인접 리스트의 마지막 노드
} AdjList;

// 전체 그래프 구조체
typedef struct
{
    int num_vertices;           // 그래프의 총 정점 수
    AdjList * adjListArr;       // 각 정점의 인접 리스트 배열
} Graph;

AdjlistNode * createNode(int v)
{
    // AdjlistNode만큼의 메모리를 동적으로 할당. 타입 캐스팅 후 newNode에 저장.
    AdjlistNode * newNode = (AdjlistNode *)malloc(sizeof(AdjlistNode));

    newNode->vertex = v;
    newNode->next = NULL;

    return newNode;
}

Graph * createGraph(int n)
{
    Graph * graph = (Graph *)malloc(sizeof(Graph));
    graph->num_vertices = n;

    graph->adjListArr = (AdjList *)malloc(n * sizeof(AdjList));

    for (int i = 0; i < n; i++)
    {
        graph->adjListArr[i].head = graph->adjListArr[i].tail = NULL;
        graph->adjListArr[i].num_members = 0;
    }

    return graph;
}

void destroyGraph(Graph * graph)
{
    if (graph)
    {
        if (graph->adjListArr)
        {
            for (int v = 0; v < graph->num_vertices; v++)
            {
                AdjlistNode * adjListPtr = graph->adjListArr[v].head;
                while (adjListPtr)
                {
                    AdjlistNode * tmp = adjListPtr;
                    adjListPtr = adjListPtr->next;
                    free(tmp);
                }
            }
            free(graph->adjListArr);
        }
        free(graph);
    }
}

void addEdge(Graph *graph, int src, int dest)
{
    AdjlistNode * newNode = createNode(dest);
    if (graph->adjListArr[src].tail != NULL)
    {
        graph->adjListArr[src].tail->next = newNode;
        graph->adjListArr[src].tail = newNode;
    }
    else
    {
        graph->adjListArr[src].head = graph->adjListArr[src].tail = newNode;
    }
    graph->adjListArr[src].num_members++;

    newNode = createNode(src);
    if (graph->adjListArr[dest].tail != NULL)
    {
        graph->adjListArr[dest].tail->next = newNode;
        graph->adjListArr[dest].tail = newNode;
    }
    else
    {
        graph->adjListArr[dest].head = graph->adjListArr[dest].tail = newNode;
    }
    graph->adjListArr[dest].num_members++;
}

void displayGraph(Graph * graph, int i)
{

    AdjlistNode * adjListPtr = graph->adjListArr[i].head;
    while (adjListPtr)
    {
        printf("%d ", adjListPtr->vertex);
        adjListPtr = adjListPtr->next;
    }
    printf("\n");
}

int main(int argc, char* argv[])
{
    int T, V, E, Q, sv, ev;

    scanf("%d", &T);

    for (int test_case = 1; test_case <= T; test_case++)
    {
        scanf("%d %d %d", &V, &E, &Q);

        Graph * graph = createGraph(V);

        for (int i = 0; i < E; i++)
        {
            scanf("%d %d", &sv, &ev);
            addEdge(graph, sv, ev);
        }
        printf("#%d\n", test_case);

        for (int i = 0; i < Q; i++)
        {
            scanf("%d", &sv);
            displayGraph(graph, sv);
        }
    }

    return 0;
}



