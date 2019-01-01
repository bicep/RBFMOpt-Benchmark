import matplotlib.pyplot as plt
from utils.utils import plot_spline, calc_local_step_perfeval

file_string = '/Users/rogerko/dev/Opossum/benchmark/benchmark' + '.txt'
csv_file_string_10 = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem4_dvar10.csv'
csv_file_string_30 = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem4_dvar30.csv'

i = 4
dim = 10
fevals = 110

# calculate the average localstep time
ave_10 = calc_local_step_perfeval(csv_file_string_10)
ave_30 = calc_local_step_perfeval(csv_file_string_30)

# against each repeated time of the
x_10 = range(0, len(ave_10))
x_30 = range(0, len(ave_30))

# plot_spline(plt, x, ave_10, len(ave_10), "10 decision var")
plot_spline(plt, x_10, ave_10, len(ave_10), "10 decision var")
plot_spline(plt, x_30, ave_30, len(ave_30), "30 decision var")

plt.legend(loc='best')
plt.title('10 v 30 decision variables (ZDT Problem ' + str(i) + ')')
plt.xlabel('Function evaluations')
plt.ylabel('Local step time (seconds)')
plt.grid()
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/zdtproblem4_10v30.png')
