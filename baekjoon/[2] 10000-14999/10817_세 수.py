A, B, C = map(int, input().split())

for _ in range(3):
    if A < B:
        A, B = B, A
    elif A < C:
        A, C = C, A
    elif B < C:
        B, C = C, B
print(B)
