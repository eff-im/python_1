# Задание 1
def squirrel(N):
    F = 1
    for i in range(1, N + 1):
        F *= i
    k = 1
    for i in range (1, len(str(F))):
        k *= 10
    pervoe_chislo = F / k
    return int(pervoe_chislo)
