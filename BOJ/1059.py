# 20220729
# 1059 좋은 구간

# S[0]보다 n이 작을 수 있음!!

L = int(input())
S = list(map(int, input().split()))
S.sort()
n = int(input())

place = -10
for i in range(len(S) - 1):
  if (S[i] < n and n < S[i + 1]):
    place = i
    break
  if (S[i] == n):
    break
  if (S[i] > n):
    place = -1

if (place == -10):
  section_num = 0
  print(section_num)
elif (place == -1):
  section_list = [i for i in range(1, S[0])]
  location = section_list.index(n)
  section_num = len(section_list) - 1 + (len(section_list) - 1 - location) * location
  print(section_num)
else:
  section_list = [i for i in range(S[i] + 1, S[i + 1])]
  location = section_list.index(n)
  section_num = len(section_list) - 1 + (len(section_list) - 1 - location) * location
  print(section_num)