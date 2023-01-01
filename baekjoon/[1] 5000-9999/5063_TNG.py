# cnt = int(input())

# for _ in range(cnt):
#     r,e,c=map(int,input().split())
#     if r < e-c:
#         print('advertise')
#     elif r == e-c:
#         print('dose not matter')
#     else:
#         print('do not advertise')

n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())
    a = e - c
    if r < a:
        print("advertise")
    elif r == a:
        print("does not matter")
    else:
        print("do not advertise")