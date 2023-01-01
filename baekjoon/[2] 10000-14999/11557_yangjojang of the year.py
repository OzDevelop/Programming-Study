# case = int(input())

# for i in range(case):
#     school= int(input())
#     alcohol = dict()
    
#     for j in range(school):
#         schoolname, bottle =input().split()
#         bottle = int(bottle)
#         alcohol[schoolname] = bottle
#     print(alcohol)
#     max = max(alcohol.values())
#     print(k for k,v in alcohol.items() if v ==max)

T = int(input())

for _ in range(T):
    N = int(input())
    alcohol = []
    
    for _ in range(N):
        S, L = map(str, input().split())
        alcohol.append([S,int(L)])
        
    alcohol = sorted(alcohol, key = lambda x: x[1])
    print(alcohol[-1][0])