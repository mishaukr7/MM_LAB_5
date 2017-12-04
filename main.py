import analytical_solution
from matplotlib import pyplot as plt
import numerical_solution

'''
FREE analytical solution
'''
# x, y = analytical_solution.analytical_method_find_solution_free(20, 44, 1.58, 40)
# plt.plot(x, y)
# plt.show()


'''
LIMITED analytical solution
'''
#x, y = analytical_solution.analytical_method_find_solution_limited(20, 44, 1.58, 78, 40)
#plt.plot(x, y)
#plt.show()

'''
FREE numerical solution
'''
# x, y = numerical_solution.numerical_solution_free(20, 44, 1.58, 78, 40, 0.1, numerical_solution.f_free)
# plt.plot(x, y)
# plt.show()

'''
LIMITED numerical solution
'''
# x, y = numerical_solution.numerical_solution_free(20, 44, 1.58, 78, 40, 0.1, numerical_solution.f_limited)
# plt.plot(x, y)
# plt.show()