# 20220802
# 11866 요세푸스 문제 0

# 문제
"""
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""

N, K = map(int, input().split())
Josephus = []
lists = [str(i + 1) for i in range(N)]
out = 0

while (len(lists) != 0):
    out = out + K - 1
    if out > len(lists) - 1:
        out = out % len(lists)
    rem = lists.pop(out)
    Josephus.append(rem)

print("<" + ", ".join(Josephus) + ">")