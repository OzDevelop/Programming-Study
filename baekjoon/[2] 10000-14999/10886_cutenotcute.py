cnt = int(input())

a = float(0)
for _ in range(cnt):
    tmp = int(input())
    a += tmp

if a / cnt > 0.5:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")