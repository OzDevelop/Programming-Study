case = int(input())

for _ in range(case):
    mars = list(map(str,input().split()))
    result = 0
    for i in range(len(mars)):
        if i ==0:
            result += float(mars[i])
        elif mars[i] == '@':
            result *= 3
        elif mars[i] == '%':
            result += 5
        elif mars[i] == '#':
            result -= 7
    print("%0.2f" %result)
