## 1~ n sum
# a = int(input())
# print("-"*10)

# result, cnt=0,  1
# for _ in range(a):
#     result += cnt
#     cnt += 1
# print(result)
#####################
# ## 진짜 쓸데없이 복잡하게 생각했네 ;;;
# S = int(input())
# cnt =2
# n= 1
# result = 1
# while True:
#     for _ in range(n):
#         result += cnt
#         cnt += 1
#         #print(result)
#     #print(n)
#     #print("--------")
#     n += 1
#     if result > S:
#         break
#     if result < S:
#         result = 0
#         cnt=2
# print(n-1)
################
s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
print(n - 1)