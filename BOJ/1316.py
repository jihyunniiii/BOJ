# 20200730
# 1316 그룹 단어 체커

N = int(input())

word_list = [input() for _ in range(N)]

group_word = 0

for word in word_list:
    exist_word = list()
    check = True

    for i in range(1, len(word)):
        if word[i - 1] != word[i]:
            for j in exist_word:
                if j == word[i]:
                    check = False
                    break
            
            if check == False:
                break

            exist_word.append(word[i - 1])
    
    if check == True:
        group_word += 1

print(group_word)