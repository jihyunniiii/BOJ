# 20220814
# 1920 수 찾기

# 문제
"""
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

def bisection(num):
    start = 0
    end = len(N_list) - 1

    while 1:
        mid = (start + end) // 2

        if start > end:
            print("0")
            break

        if num == N_list[mid]:
            print("1")
            break

        elif N_list[mid] > num:
            end = mid - 1
        
        elif N_list[mid] < num:
            start = mid + 1

for i in M_list:
    bisection(i)