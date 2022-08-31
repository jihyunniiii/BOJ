# 20220831
# 24479 알고리즘 수업 - 깊이 우선 탐색 1

# 문제
"""
오늘도 서준이는 깊이 우선 탐색(DFS) 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.

깊이 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

dfs(V, E, R) {  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited[R] <- YES;  # 시작 정점 R을 방문 했다고 표시한다.
    for each x ∈ E(R)  # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if (visited[x] = NO) then dfs(V, E, x);
}
"""

import sys
sys.setrecursionlimit(10**7)

N, M, R = map(int, sys.stdin.readline().rstrip().split())

edge = list()

for _ in range(M):
    edge.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

edge.sort()

adj = [[] for _ in range(N)]

for i in edge:
    adj[i[0] - 1].append(i[1] - 1)
    adj[i[1] - 1].append(i[0] - 1)

visited = [0] * N
global num
num = 1

def dfs(v):
    global num
    visited[v] = num
    num += 1

    for i in adj[v]:
        if visited[i] == 0:
            dfs(i)

dfs(R - 1)

for j in visited:
    print(j)