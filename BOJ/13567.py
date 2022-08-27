# 20220827
# 13567 로봇

# 문제
"""
로봇은 명령어를 읽어들여 정사각형 영역 S를 x축 또는 y축과 평행한 방향으로 움직인다. S의 왼쪽 아래 꼭짓점은 (0, 0)이고, 오른쪽 위의 꼭짓점은 (M, M)이다. 처음에 로봇은 (0, 0)에 위치해 있고, 동쪽 방향을 향하고 있다.

명령어는 로봇이 현재 위치에서 행할 동작과 그 동작과 관련된 값으로 주어진다. 동작은 두 가지가 있는데, TURN과 MOVE이다. TURN 0 명령은 현재 위치에서 왼쪽으로 90도 회전, TURN 1 명령은 현재 위치에서 오른쪽으로 90도 회전을 의미한다. MOVE d 명령은 로봇이 향하고 있는 방향으로 d만큼 움직이는 것을 의미한다. 여기서 d는 양수이다.

명령의 수행 후 로봇이 S의 경계 또는 내부에 있으면 이 명령어는 유효하다. 만일 명령어 수행 후 로봇이 S의 바깥으로 완전히 나가게 된다면 명령어는 유효하지 않다. 일련의 명령어 열을 이루는 각 명령어가 모두 유효하다면, 이 명령어 열을 유효하다고 한다.

예를 들어 로봇이 왼쪽 그림과 같이 (MOVE 6, TURN 0, MOVE 5, TURN 0, MOVE 2, TURN 0, MOVE 2, TURN 0, MOVE 4, TURN 0, MOVE 3, MOVE 2) 명령어를 읽어들인다면, 최종적으로 로봇은 (8, 8) 위치에 있게 된다. 가운데 그림과 같이 (MOVE 10, TURN 0, MOVE 2, TURN 0, MOVE 5, TURN 1, MOVE 5, TURN 1, MOVE 2, TURN 1, MOVE 3, TURN 0, TURN 0, MOVE 6) 명령어를 읽어들인다면, 로봇은 (7, 10)에 위치하게 된다. 오른쪽 그림과 같이 로봇이 S 바깥으로 나간다면, 명령어 열은 유효하지 않다.

한 변의 길이가 M인 정사각형과 n개의 명령어, 그리고 로봇이 (0, 0) 위치에서 시작해 동쪽을 바라보고 있을 때, n개의 명령어를 따라 움직였을 때 최종 위치를 출력하는 프로그램을 작성하라
"""

import sys

M, n = map(int, sys.stdin.readline().rstrip().split())

robot = [0, 0]
move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
move_value = 0
check = 0

for _ in range(n):
    command, value = sys.stdin.readline().rstrip().split()
    value = int(value)

    if command == "MOVE":
        robot[0] += move[move_value][0] * value
        robot[1] += move[move_value][1] * value

        if robot[0] < 0 or robot[0] > M or robot[1] < 0 or robot[1] > M:
            check = 1
            
    elif command == "TURN":
        if value == 0:
            move_value = (move_value - 1) % 4
        elif value == 1:
            move_value = (move_value + 1) % 4

if check == 1:
    print("-1")
else:
    print(f"{robot[0]} {robot[1]}")
