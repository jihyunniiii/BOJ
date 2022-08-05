# 20220805
# 1789 수들의 합

# 문제
"""
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
"""

N = int(input())
sum = 0
num = 0

while N >= sum:
    num += 1
    sum += num
    
print(num - 1)