# 20220920
# 1697 숨바꼭질

# 문제
"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100000

location = [0 for _ in range(MAX + 1)]

def BFS(num):
    queue = deque()
    queue.append(num)

    while(queue):
        temp = queue.popleft()

        if temp == K:
            break

        if  0 <= temp - 1 <= MAX and location[temp - 1] == 0:
            location[temp - 1] = location[temp] + 1
            queue.append(temp - 1)
        
        if 0 <= temp + 1 <= MAX and location[temp + 1] == 0:
            location[temp  + 1] = location[temp] + 1
            queue.append(temp + 1)

        if 0 <= temp * 2 <= MAX and location[temp * 2] == 0:
            location[temp * 2] = location[temp] + 1
            queue.append(temp * 2)
        
BFS(N)

print(location[K])