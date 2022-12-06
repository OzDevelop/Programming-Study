point = int(input())

if point >= 90:
    print("A")
elif point < 90 and point >= 80:
    print("B")
elif point <80 and point >= 70:
    print("C")
elif point <70 and point >= 60:
    print("D")
else:
    print("F")