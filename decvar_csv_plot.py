import matplotlib.pyplot as plt
from utils.utils import plot_spline, calc_local_step_perfeval

problem_number = 4
dvar = 10
dvar2 = 30
fevals = 200

csv_file_string_10 = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem' + str(problem_number) + '_dvar' + str(dvar) + '_feval' + str(fevals) + '.csv'

csv_file_string_30 = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem' + str(problem_number) + '_dvar' + str(dvar2) + '_feval' + str(fevals) + '.csv'

# csv_file_string_10 = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem4_dvar10_feval200.csv'
# csv_file_string_30 = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem4_dvar30_feval200.csv'

fevals = 200

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
plt.title('10 v 30 decision variables (ZDT Problem ' + str(problem_number) + ')')
plt.xlabel('Function evaluations')
plt.ylabel('Local step time (seconds)')
plt.grid()
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/zdtproblem4_10v30_fevals200.png')
