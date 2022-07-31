# 20220731
# 1181 단어 정렬

# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

# 딕셔너리 value 값을 기준으로 정렬하는 법
# sorted(word_list.items(), key = lambda x: x[1])
# 위와 같이 lambda 함수를 이용함 (lambda 함수 = 익명 함수 => 함수를 선언하지 않고 lambda 식으로 대체함)

N = int(input())

word_list = {}

for _ in range(N):
    value = input()
    word_list[value] = len(value)

word_list = sorted(word_list.items())

new_list = {}
for i in range(len(word_list)):
    new_list[word_list[i][0]] = word_list[i][1]

new_list = sorted(new_list.items(), key = lambda x: x[1])

for i in range(len(new_list)):
    print(new_list[i][0])