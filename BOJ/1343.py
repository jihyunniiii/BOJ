# 20220813
# 1343 폴리오미노

# 문제
"""
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.
"""

board = input().split(".")

check = 0
for i in range(len(board)):
    str_temp = list(board[i])
    length = len(str_temp)
    if length == 0:
        continue

    if length % 2 == 1:
        check = 1
        break
    
    temp = 0
    while(length > temp):
        if length - temp >= 4:
            str_temp[temp:temp + 4] = "AAAA"
            temp += 4
        elif length - temp >= 2:
            str_temp[temp:temp + 2] = "BB"
            temp += 2
    
    board[i] = "".join(str_temp)

if check == 1:
    print("-1")
else:
    print(".".join(board))