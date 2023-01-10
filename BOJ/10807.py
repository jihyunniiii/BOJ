# 20230110
# 10807 개수 세기

# 문제
"""
총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오
"""

import sys

N = int(sys.stdin.readline())

N_list = list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline())

print(N_list.count(v))