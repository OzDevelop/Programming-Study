while True:
    a, b = map(int,input().split())
    if a > b:
        print("Yes")
    elif a<b or (a==b and a !=0):
        print("No")
    elif a==b and b==0:
        break