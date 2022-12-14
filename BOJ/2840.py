# 20220827
# 2840 행운의 바퀴

# 문제
"""
상덕이는 최근에 행운의 바퀴를 구매했다. 상덕이는 바퀴의 각 칸에 알파벳 대문자를 아래 그림과 같이 적었다.

바퀴에 같은 글자는 두 번 이상 등장하지 않는다. 또, 바퀴는 시계방향으로만 돌아간다. 바퀴 옆에는 화살표가 있는데, 이 화살표는 항상 한 곳을 가리키고 있으며, 돌아가는 동안 가리키는 글자는 바뀌게 된다. 위의 그림에서는 H를 가리키고 있다.

상덕이는 바퀴를 연속해서 K번 돌릴 것이다. 매번 바퀴를 돌릴 때 마다, 상덕이는 화살표가 가리키는 글자가 변하는 횟수와 어떤 글자에서 회전을 멈추었는지를 종이에 적는다.

희원이는 상덕이가 적어놓은 종이를 발견했다. 그 종이를 바탕으로 상덕이가 바퀴에 적은 알파벳을 알아내려고 한다.

상덕이가 종이에 적어놓은 내용과 바퀴의 칸의 수가 주어졌을 때, 바퀴에 적어놓은 알파벳을 알아내는 프로그램을 작성하시오.
"""

import sys

N, K = map(int, sys.stdin.readline().split())

whell = ["?"] * N

temp = 0
check = 0
for _ in range(K):
    S, letter = sys.stdin.readline().split()

    temp = (temp + int(S)) % N
    
    if whell[temp] == "?":
        if letter in whell:
            check = 1
            break
        whell[temp] = letter
    elif whell[temp] != letter:
        check = 1
        break

if check == 1:
    print("!")
else:
    output = ""
    for _ in range(N):
        output += whell[temp]
        temp = (temp - 1) % N
    print(output)