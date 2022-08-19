# 20220818
# 2422 한윤정이 이탈리아에 가서 아이스크림을 사먹는데

# 문제
"""
한윤정과 친구들은 이탈리아로 방학 여행을 갔다. 이탈리아는 덥다. 윤정이와 친구들은 아이스크림을 사먹기로 했다. 아이스크림 가게에는 N종류의 아이스크림이 있다. 모든 아이스크림은 1부터 N까지 번호가 매겨져있다. 어떤 종류의 아이스크림을 함께먹으면, 맛이 아주 형편없어진다. 따라서 윤정이는 이러한 경우를 피하면서 아이스크림을 3가지 선택하려고 한다. 이때, 선택하는 방법이 몇 가지인지 구하려고 한다.
"""

import sys
from itertools import combinations

N, M = map(int, input().split())
M_list = [[True] * N for _ in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    M_list[i - 1][j - 1] = False
    M_list[j - 1][i - 1] = False

num = 0
for i in list(combinations(range(N), 3)):
    if M_list[i[0]][i[1]] and M_list[i[0]][i[2]] and M_list[i[1]][i[2]]:
        num += 1

print(num)