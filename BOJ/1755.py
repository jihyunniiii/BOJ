# 20220820
# 1755 숫자놀이

# 문제
"""
79를 영어로 읽되 숫자 단위로 하나씩 읽는다면 "seven nine"이 된다. 80은 마찬가지로 "eight zero"라고 읽는다. 79는 80보다 작지만, 영어로 숫자 하나씩 읽는다면 "eight zero"가 "seven nine"보다 사전순으로 먼저 온다.

문제는 정수 M, N(1 ≤ M ≤ N ≤ 99)이 주어지면 M 이상 N 이하의 정수를 숫자 하나씩 읽었을 때를 기준으로 사전순으로 정렬하여 출력하는 것이다.
"""
M, N = map(int, input().split())

number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

eng_num = []
for i in range(M, N + 1):
    if len(str(i)) == 2:
        eng_num.append((number[i // 10] + number[i % 10], i))
    else:
        eng_num.append((number[i], i))

eng_num.sort()

for i in range(len(eng_num)):
    if i % 10 == 9:
        print(eng_num[i][1])
    else:
        print(eng_num[i][1], end = " ")