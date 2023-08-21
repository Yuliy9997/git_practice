import math

n = int(input('Введите количесиво знаков послле запятой: '))
 
pi = math.pi

print("{:.{precision}f}".format(pi, precision=n))

# some changes