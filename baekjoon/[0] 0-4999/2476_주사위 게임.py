
N = int(input())
lst = []
for i in range(N):
    tmp = 0 
    a, b, c = list(map(int, input().split()))

    if a == b == c:
        tmp =10000 + a * 1000
    elif a == b:
        tmp = 1000+ b*100
    elif b == c:
        tmp = 1000+ b*100
    elif c == a:
        tmp = 1000+ c*100
    else:
        tmp = max(a, b, c)*100
    lst.append(tmp)
print(max(lst))