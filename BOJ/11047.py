# 20220813
# 11047 동전 0

# 문제
"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
"""

import sys

N, K = map(int, input().split())
N_list = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

N_list.sort(reverse = True)

num = 0
for i in N_list:
    if i <= K:
        num += K // i
        K -= (K // i) * i
    if K <= 0:
        break

print(num)