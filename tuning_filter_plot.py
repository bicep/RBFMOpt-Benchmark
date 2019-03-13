import math
import matplotlib.pyplot as plt
import numpy as np
from utils.utils import plot_spline, load_values, normalize

n = 5
dim = 30
cycle = 3 
max_fevals = (dim+1) * 50

fevals_plot = range(100, max_fevals)
fig, ax = plt.subplots()

x_labels = [str(3*dim), str(6*dim), str(9*dim), str(None)]

storedvals = {
  str(3*dim): [],
  str(6*dim): [],
  str(9*dim): [],
  str(None): []
}

boxplots = []

# For the 4 zdt problems
for i in range(6):

    problem_number = i+1

    if i == 4:
        continue
    elif i == 5:
        # Hack because we skip problem 5 but we use problem 5's array index for problem 6
        i = 4

    maxi = -math.inf
    mini = math.inf

    for x in x_labels:
        for run in range(n):
            storedvals[x].append(load_values('store_hv/rbfmopt_hv_ncycle' + str(cycle) + '_filter' + x + '_fevals' + str(max_fevals) + 'ZDT' + str(problem_number) + '_run' + str(run+1) + '.txt'))

            # i is the (problem_number -1), get the max and min for the problem
            maxi = max(max(storedvals[x][(i*n)+run]), maxi)
            mini = min(min(storedvals[x][(i*n)+run]), mini)

    # normalize and replace original values
    for x in x_labels:
        for run in range(n):
            storedvals[x][(i*n)+run] = normalize(storedvals[x][(i*n)+run], maxi, mini)

# calc the mean of the normalized values
for x in x_labels:
    median_hv = np.median(storedvals[x], axis=0)
    boxplots.append([i[max_fevals-1] for i in storedvals[x]])
    plot_spline(plt, fevals_plot, median_hv[100:], max_fevals, x, 100)

plt.legend(loc='best')
plt.title('Tuning between 90, 180, 270 and no filter')
plt.xlabel('Function evaluations')
plt.ylabel('Median hypervolume over '+str(n)+' runs')
plt.grid()
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Tuning_filter_graph_median' + '.png', dpi=300)

plt.clf()

plt.title('Tuning between 90, 180, 270 and no filter')
plt.boxplot(boxplots)
plt.xticks([1, 2, 3, 4], ['90', '180', '270', 'None'])
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Tuning_filter_boxplot_median' + '.png', dpi=300)
