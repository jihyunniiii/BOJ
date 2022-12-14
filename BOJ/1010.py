# 20220729
# 1010 다리 놓기

fact = [0] * 31
fact[0] = 1

for i in range(1, 31):
  fact[i] = fact[i - 1] * i
  
T = int(input())

lists = [input() for _ in range(T)]

for i in lists:
  N, M = map(int, i.split())
  print(int(fact[M] / (fact[M - N] * fact[N])))