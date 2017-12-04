import math


def analytical_method_find_solution_free(t0, N0, r, T):
    N = []
    time = []
    for t in range(t0, T+1):
        N_new = N0*math.exp(r*(t-20))
        N.append(N_new)
        time.append(t)
    return time, N


def analytical_method_find_solution_limited(t0, N0, r, k, T):
    N = []
    time = []
    for t in range(t0, T):
        N_new = (k * N0 * math.exp(r * (t - 20)))/(k + N0 * (math.exp(r * (t - 20)) - 1))
        N.append(N_new)
        time.append(t)
    return time, N
