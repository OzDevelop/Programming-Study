def GCD(x, y):
    while(y):
        x, y=y, x%y
    return x

def LCM(x, y):
    result = (x*y)//GCD(x,y)
    return result

cnt = int(input())

for _ in range(cnt):
    x, y = map(int, input().split())
    print(LCM(x,y))
