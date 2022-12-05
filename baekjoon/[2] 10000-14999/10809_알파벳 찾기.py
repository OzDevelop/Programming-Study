from string import ascii_lowercase          #alphabet 

alphabet_list = list(ascii_lowercase)

S = input("")

for list in alphabet_list:
    if list in S:
        print(S.index(list), end=' ')
    else:
        print(-1, end=' ')

##또 다른 사람 코드
# S = input()
# check = [-1]*26
 
# for i in range(len(S)):
#     if check[ord(S[i])-97] != -1:
#         continue
#     else:
#         check[ord(S[i])-97] = i
        
# for i in range(26):
#     print(check[i], end=' ')