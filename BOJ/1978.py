# 20200730
# 1978 소수 찾기

N = int(input())

N_list = list(map(int, input().split()))

num = 0
for N in N_list:
    check = True

    if N == 1:
        check = False

    for i in range(2, N):
        if N % i == 0:
            check = False
    
    if check == True:
        num += 1

print(num)