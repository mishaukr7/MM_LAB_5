import analytical_solution
from matplotlib import pyplot as plt
import numerical_solution

t0 = 20
N0 = 44
r = 1.58
k = 78
T = 40
h = 0.1


'''
FREE analytical solution
'''
# x, y = analytical_solution.analytical_method_find_solution_free(t0, N0, r, T)
# plt.plot(x, y)
# plt.show()


'''
LIMITED analytical solution
'''
#x, y = analytical_solution.analytical_method_find_solution_limited(t0, N0, r, k, T)
#plt.plot(x, y)
#plt.show()

'''
FREE numerical solution
'''
# x, y = numerical_solution.numerical_solution_free(t0, N0, r, k, T, h, numerical_solution.f_free)
# plt.plot(x, y)
# plt.show()

'''
LIMITED numerical solution
'''
# x, y = numerical_solution.numerical_solution_free(t0, N0, r, k, T, h, numerical_solution.f_limited)
# plt.plot(x, y)
# plt.show()