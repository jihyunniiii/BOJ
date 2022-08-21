# 20220821
# 2578 빙고

# 문제
"""
빙고 게임은 다음과 같은 방식으로 이루어진다.

먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 1부터 25까지 자연수를 한 칸에 하나씩 쓴다

다음은 사회자가 부르는 수를 차례로 지워나간다. 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.

차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.

이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 가장 먼저 외치는 사람이 게임의 승자가 된다.

철수는 친구들과 빙고 게임을 하고 있다. 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 출력하는 프로그램을 작성하시오.
"""

import sys

bingo = dict()

j = -1
for _ in range(5):
    j += 1
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(len(temp)):
        bingo[temp[i]] = (j, i)

number = list()

for _ in range(5):
    number += list(map(int, sys.stdin.readline().rstrip().split()))

check = [[False] * 5 for _ in range(5)]

for i in range(len(number)):
    num = 0
    temp = bingo[number[i]]
    check[temp[0]][temp[1]] = True

    if check[0][0] and check[1][1] and check[2][2] and check[3][3] and check[4][4]:
        num += 1
    
    if check[0][4] and check[1][3] and check[2][2] and check[3][1] and check[4][0]:
        num += 1

    for j in range(5):
        if check[j][0] and check[j][1] and check[j][2] and check[j][3] and check[j][4]:
            num += 1
        
        if check[0][j] and check[1][j] and check[2][j] and check[3][j] and check[4][j]:
            num += 1
    
    if num >= 3:
        print(i + 1)
        break