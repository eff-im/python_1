# Задание 1
def squirrel(N):
    F = 1
    for i in range(1, N + 1):
        F *= i
    return F

