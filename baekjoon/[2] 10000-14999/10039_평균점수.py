point = []
for i in range(5):
   point.append(int(input()))
   if point[i] <= 40:
       del point[i]
       point.append(40)

result = sum(point)
print(int(result/len(point)))
