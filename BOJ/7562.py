# 20220920
# 7562 나이트의 이동

# 문제
"""
체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?
"""

import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
answer = list()

def BFS(i, j, l):
    dx = [+1, +2, +2, +1, -1, -2, -2, -1]
    dy = [+2, +1, -1, -2, -2, -1, +1, +2]
    queue = deque()
    queue.append([i, j])

    while queue:
        temp = queue.popleft()

        if temp == end:
            break

        for i in range(8):
            if 0 <= temp[0] + dy[i] < l and 0 <= temp[1] + dx[i] < l and size[temp[0] + dy[i]][temp[1] + dx[i]] == 0:
                size[temp[0] + dy[i]][temp[1] + dx[i]] = size[temp[0]][temp[1]] + 1
                queue.append([temp[0] + dy[i], temp[1] + dx[i]])

for _ in range(T):
    l = int(sys.stdin.readline().rstrip())

    size = [[0 for _ in range(l)] for _ in range(l)]

    now = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))
    
    BFS(now[0], now[1], l)
    answer.append(size[end[0]][end[1]])

for i in answer:
    print(i)