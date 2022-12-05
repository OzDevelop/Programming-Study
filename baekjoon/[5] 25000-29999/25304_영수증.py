price = int(input())
num = int(input())

for i in range(num):
    price1, count = input().split()
    price1, count = int(price1), int(count)

    price -= (price1*count)

print("Yes" if price==0 else "No")
