hour, min = input().split()
hour = int(hour)
min = int(min)

time = int(input())

min1 = min + time

if min1 >=60:
    hour = int(hour + (min1 / 60))
    min = min1 % 60
    
    if hour >= 24:
        hour = hour-24

elif min1 < 60:
        min = min1

print(hour,min)

## 딴 사람한거
# h, m = map(int, input().split())
# t = int(input()) 

# h += t // 60
# m += t % 60

# if m >= 60:
#     h += 1
#     m -= 60
# if h >= 24:
#     h -= 24

# print(h, m)