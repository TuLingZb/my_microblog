import math


def sqrt_newton(num, p):
    """
    num为待开方数字
    p为给定的精度，例如1e-5
    """
    if num == 0:
        return 0
    x = num / 2
    while abs(x ** 2 - num) > p:
        x = (x + num / x) / 2
    return int(x)

a = sqrt_newton(8,1e-5)
print(a)
