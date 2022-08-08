# 20220808
# 7785 회사에 있는 사람

# 문제
"""
상근이는 세계적인 소프트웨어 회사 기글에서 일한다. 이 회사의 가장 큰 특징은 자유로운 출퇴근 시간이다. 따라서, 직원들은 반드시 9시부터 6시까지 회사에 있지 않아도 된다.

각 직원은 자기가 원할 때 출근할 수 있고, 아무때나 퇴근할 수 있다.

상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
"""

# sys.stdin.readline()
# 반복문으로 여러줄을 입력받는 경우 input()보다 sys.stdin.readline() 사용하는 거 추천
# sys.stdin.readline()이 input()보다 걸리는 시간이 더 적음
# 하지만 sys.stdin.readline()은 한 줄 단위로 입력을 받기 때문에 개행문자가 같이 입력받아짐 -> 개행문자 제거하는 것 필요

import sys

n = int(input())

enter_log = {}

for _ in range(n):
    name, enter = sys.stdin.readline().rstrip().split()
    
    if enter == "enter":
        enter_log[name] = enter
    else:
        del enter_log[name]
    
enter_log = sorted(enter_log.keys(), reverse=True)

for i in enter_log:
    print(i)