# 20220816
# 10825 국영수

# 문제
"""
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
"""

import sys

N = int(input())

student = dict()

for _ in range(N):
    name, korea, english, math = sys.stdin.readline().rstrip().split()

    english = str(100 - int(english))

    if len(korea) == 2:
        korea = '0' + korea
    elif len(korea) == 1:
        korea = '00' + korea

    if len(english) == 2:
        english = '0' + english
    elif len(english) == 1:
        english = '00' + english

    if len(math) == 2:
        math = '0' + math
    elif len(math) == 1:
        math = '00' + math

    student[name] = int(korea + english + math)

student = sorted(student.items(), key = lambda x : (-x[1], x[0]))

for i in range(len(student)):
    print(student[i][0])