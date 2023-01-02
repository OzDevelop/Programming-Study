# def getDivisor(n, divisor):
#     for i in range(1, n+1):
#         if n % i == 0:
#             divisor.append(i)
#     del divisor[-1]

# while True:
#     divisor = []
#     n = int(input())
#     getDivisor(n, divisor)

#     if n == -1:
#         break
#     if sum(divisor) == n:
#         print(n, " = ", " + ".join(str(i) for i in divisor), sep="")
#     else:
#         print(n, "is NOT perfect.")
    

while True:
    divisor = []
    n = int(input())
    if n == -1:
        break

    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    del divisor[-1]

    if sum(divisor) == n:
        print(n, " = ", " + ".join(str(i) for i in divisor), sep="")
    else:
        print(n, "is NOT perfect.")
    