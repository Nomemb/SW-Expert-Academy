"""
V개 이내의 노드를 E 개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때,
특정 두 개의 노드에 경로가 존재하는 지 확인하는 프로그램을 만드시오.

경로가 있으면 1, 없으면 0
"""

T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for i in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)

    S, G = map(int, input().split())

    stack = []
    visited = [False] * (V+1)

    stack.append(S)
    visited[S] = True

    is_connected = False
    while stack and not is_connected:
        cur = stack.pop()
        for w in graph[cur]:
            if not visited[w]:
                if w == G:
                    is_connected = True
                    break

                visited[w] = True
                stack.append(w)

    print(f"#{tc} 1" if is_connected else f"#{tc} 0")
