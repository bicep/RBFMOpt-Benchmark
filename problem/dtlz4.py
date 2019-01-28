import math as math


def dtlz4(x, alpha=100):
    i = 0
    j = 0
    n = len(x)
    k = n - 2 + 1
    # no of obj
    M = 2

    g = 0

    for h in range(n-k+1, n):
        g += (x[h-1] - 0.5)**2

    fx = [None] * M

    for i in range(1, M+1):
        f = g+1
        for j in range(M-i, 0, -1):
            f *= math.cos(x[j-1]**alpha * math.pi / 2)
        if i > 1:
            f *= math.sin((x[M-1+1]-1)**alpha * math.pi / 2)
        fx[i-1] = f

    return fx
