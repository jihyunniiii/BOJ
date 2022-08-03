# 20220803
# 10815 숫자 카드

# 문제
"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
"""

# 이분 탐색
# 정렬된 리스트 안에서 원하는 숫자를 찾아가는 알고리즘

N = int(input())
N_card = list(map(int, input().split()))
M = int(input())
M_card = list(map(int, input().split()))

N_card.sort()

def binary_search(lists, num):
    start = 0
    end = len(lists) - 1

    while start <= end:
        mid = (start + end) // 2

        if num == lists[mid]:
            print("1", end = " ")
            return
        elif num < lists[mid]:
            end = mid - 1
        else:
            start = mid + 1

    print("0", end = " ")

for i in M_card:
    binary_search(N_card, i)