import math

N = int(input('N = '))

divide = []

for i in range(2, N + 1):
    while N % i == 0:
        divide.append(i)
        N //= i

print(*divide, sep=' * ')


n = int(input('Введите количесиво знаков послле запятой: '))
 
pi = math.pi

print("{:.{precision}f}".format(pi, precision=n))

# some changes