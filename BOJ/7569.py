# 20220922
# 7569 토마토

# 문제
"""
철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자모양 상자의 칸에 하나씩 넣은 다음, 상자들을 수직으로 쌓아 올려서 창고에 보관한다.

창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
"""

import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomato = [[] for _ in range(H)]

for h in range(H):
    for _ in range(N):
        tomato[h].append(list(map(int, sys.stdin.readline().split())))

def BFS():
    dx = [0, 0, 0, 0, 1, -1]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [1, -1, 0, 0, 0, 0]

    queue = deque()

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato[i][j][k] == 1:
                    queue.append([i, j, k])
    
    while queue:
        temp = queue.popleft()

        for t in range(6):
            x = temp[1] + dx[t]
            y = temp[2] + dy[t]
            z = temp[0] + dz[t]

            if 0 <= z < H and 0 <= x < N and 0 <= y < M and tomato[z][x][y] == 0:
                tomato[z][x][y] = tomato[temp[0]][temp[1]][temp[2]] + 1
                queue.append([z, x, y])
            
BFS()

check = 0
answer = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                check = 1
                break
            answer = max(answer, tomato[i][j][k])

if check == 1:
    print(-1)
elif answer == -1:
    print(0)
else:
    print(answer - 1)