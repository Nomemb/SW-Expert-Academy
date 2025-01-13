"""
비선형 구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 게 중요.

DFS(깊이 우선 탐색)
    stack 사용
    시작 정점의 한 방향으로 끝까지 탐색
    더 이상 갈 곳 없으면 가장 마지막 간선이 있던 정점으로 되돌아 옴.

    1. 시작 정점 v를 결정해 방문
    2. 해당 v에 인접한 정점 중, 방문하지 않은 정점 w가 있으면 v를 스택에 push하고 w를 방문
    3. w를 v로 해 1을 반복

    4. 방문하지 않은 정점이 없으면, 스택을 pop해 받은 마지막 방문 정점을 v로 해 다시 1 반복
"""

graph = [
    [],
    [2, 3],
    [1, 4, 5],
    [1, 5],
    [2, 6],
    [2, 3, 6],
    [4, 5, 7],
    [6]
]


visited = [False] * len(graph)
stack = []

def dfs(v):
    stack.append(v)
    visited[v] = True

    while stack:
        v = stack.pop()
        print(v)
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                stack.append(w)



dfs(1)