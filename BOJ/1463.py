# 20220830
# 1463 1로 만들기

# 문제
"""
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.
정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

import sys

N = int(sys.stdin.readline().rstrip())

numberoftime = [0, 0, 1, 1]

for i in range(4, N + 1):
    numberoftime.append(numberoftime[i - 1] + 1)

    if i % 3 == 0:
        numberoftime[i] = min(numberoftime[i // 3] + 1, numberoftime[i])
    
    if i % 2 == 0:
        numberoftime[i] = min(numberoftime[i // 2] + 1, numberoftime[i])

print(numberoftime[N])