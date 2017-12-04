import math


def f_free(r, N, *k):
    return r * N


def f_limited(r, N, *k):
    k = k[0]
    return r*N*(1 - N/int(k))


def numerical_solution(t0, N0, r, k, T, h, f):
    N = [N0]
    i = 0
    t = [t0]
    while t[i] < T:
        k_1 = f(r, N[i], k)
        k_2 = f(r, N[i] + h * k_1 / 2, k)
        k_3 = f(r, N[i] + h * k_2 / 2, k)
        k_4 = f(r, N[i] + h * k_3, k)
        N.append(N[i] + h * (k_1 + 2 * k_2 + 2 * k_3 + k_4) / 6)
        t.append(t[i] + h)
        i += 1
    return t, N


