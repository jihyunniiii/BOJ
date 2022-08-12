# 20220812
# 5635 생일

# 문제
"""
어떤 반에 있는 학생들의 생일이 주어졌을 때, 가장 나이가 적은 사람과 가장 많은 사람을 구하는 프로그램을 작성하시오.
"""
import sys

n = int(input())

births = dict()

for _ in range(n):
    name, day, month, year = sys.stdin.readline().rstrip().split()
    if len(month) < 2:
        month = "0" + month
    if len(day) < 2:
        day = "0" + day
    
    birth = year + month + day

    births[name] = birth

births = sorted(births.items(), key = lambda x: x[1], reverse = True)

print(births[0][0])
print(births[-1][0])