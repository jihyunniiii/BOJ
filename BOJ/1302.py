# 20220818
# 1302 베스트 셀러

# 문제
"""
김형택은 탑문고의 직원이다. 김형택은 계산대에서 계산을 하는 직원이다. 김형택은 그날 근무가 끝난 후에, 오늘 판매한 책의 제목을 보면서 가장 많이 팔린 책의 제목을 칠판에 써놓는 일도 같이 하고 있다.

오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때, 가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
"""

import sys

N = int(input())
N_list = dict()

for _ in range(N):
    name = sys.stdin.readline().rstrip()

    N_list[name] = N_list.get(name, 0) + 1

N_list = sorted(N_list.items(), key = lambda x : x[0])
N_list = sorted(N_list, key = lambda x : x[1], reverse = True)

print(N_list[0][0])