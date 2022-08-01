# 20220801
# 2941 크로아티아 알파벳

# 문제
"""
예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
"""

# 지정 문자열 삭제
# 문자열.replace(치환하고 싶은 문자열, 새로운 문자, 치환 횟수) => 새로운 문자를 ""로 설정하면 됨

# 문자열에서 단어 수 세기
# 문자열.count(찾고 싶은 단어, start, end)

alphabet = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

i = 0
alphabet_num = 0

for check_alphabet in croatia:
    if check_alphabet in alphabet:
        count_alphabet = alphabet.count(check_alphabet)
        alphabet_num += count_alphabet
        alphabet = alphabet.replace(check_alphabet, " ", count_alphabet)

alphabet = alphabet.replace(" ", "")
alphabet_num = alphabet_num + len(alphabet)

print(alphabet_num)