import os
import math
import matplotlib.pyplot as plt
import numpy as np
from utils.utils import plot_spline, load_values, normalize

n = 10
dim = 30
cycle = 3 
max_fevals = (dim+1) * 50

starting = 150

fevals_plot = range(starting, max_fevals)
fig, ax = plt.subplots()

x_labels = [str(3), str(6), str(9)]

storedvals = {
  str(3): [],
  str(6): [],
  str(9): [],
}

boxplots = []
cwd = os.getcwd()

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
            storedvals[x].append(load_values('storedvalues/rbfmopt_hv_ncycle' + x + '_filter' + 'None' + '_fevals' + str(max_fevals) + 'ZDT' + str(problem_number) + '_run' + str(run+1) + '.txt'))

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
    plot_spline(plt, fevals_plot, median_hv[starting:], max_fevals, x, starting)

plt.legend(loc='best')
plt.title('Tuning between 3, 6 and 9 ncycles')
plt.xlabel('Function evaluations')
plt.ylabel('Median hypervolume over '+str(n)+' runs')
plt.grid()
plt.savefig(cwd + '/graphics/Tuning_ncycle_graph_median' + '.png', dpi=300)

plt.clf()

plt.title('Tuning between 3, 6 and 9 ncycles')
plt.boxplot(boxplots)
plt.xticks([1, 2, 3], ['3', '6', '9'])
plt.savefig(cwd + '/graphics/Tuning_ncycle_boxplot_median' + '.png', dpi=300)
