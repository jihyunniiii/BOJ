# 20220805
# 10867 중복 빼고 정렬하기

# 문제
"""
N개의 정수가 주어진다. 이때, N개의 정수를 오름차순으로 정렬하는 프로그램을 작성하시오. 같은 정수는 한 번만 출력한다.
"""

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

temp = nums[0]
print(temp, end=" ")

for i in range(1, len(nums)):
    if temp != nums[i]:
        temp = nums[i]
        print(temp, end=" ")
