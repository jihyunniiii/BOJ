# 20200915
# 1260 DFS와 BFS

# 문제
"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().rstrip().split())

edge = list()

for _ in range(M):
    edge.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

adj = [[] for _ in range(N)]

for i in edge:
    adj[i[0] - 1].append(i[1] - 1)
    adj[i[1] - 1].append(i[0] - 1)

for i in adj:
    i.sort()

dfs_visited = [0 for _ in range(N)]

def dfs(V):
    dfs_visited[V] = 1
    print(V + 1, end = " ")

    for i in adj[V]:
        if dfs_visited[i] == 0:
            dfs(i)

bfs_visited = [0 for _ in range(N)]
queue = deque()

def bfs(V):
    bfs_visited[V - 1] = 1
    queue.append(V)

    while (queue):
        temp = queue.popleft()
        print(temp, end = " ")

        for i in adj[temp - 1]:
            if bfs_visited[i] == 0:
                bfs_visited[i] = 1
                queue.append(i + 1)

dfs(V - 1)
print()
bfs(V)