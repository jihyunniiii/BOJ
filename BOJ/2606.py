# 20220831
# 2606 바이러스

# 문제
"""
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.



어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.
"""

import sys

N = int(sys.stdin.readline().rstrip())

adj_matrix = [[0] * N for _ in range(N)]

num = int(sys.stdin.readline().rstrip())

for _ in range(num):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    adj_matrix[a - 1][b - 1] = 1
    adj_matrix[b - 1][a - 1] = 1

visited = [0] * N
visited_node = []

def dfs(node):
    visited[node] = 1
    visited_node.append(node)

    for i in range(N):
        if adj_matrix[node][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(0)

print(len(visited_node) - 1)