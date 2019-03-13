import os
import math
import matplotlib.pyplot as plt
import numpy as np
from utils.utils import plot_spline, load_values, normalize

n = 10
n_prob = 7
dim = 30
n_cycle = 6
n_filter = 180
max_fevals = (dim+1) * 50

fevals_plot = range(0, max_fevals)
fig, ax = plt.subplots()

x_labels = ['rbfmopt', 'MOEAD', 'NSGA-II']

storedvals = {
  x_labels[0]: [],
  x_labels[1]: [],
  x_labels[2]: [],
}

boxplots = []
cwd = os.getcwd()


# For the 4 zdt problems
for i in range(n_prob):

    problem_number = i+1

    maxi = -math.inf
    mini = math.inf

    for x in x_labels:
        for run in range(n):
            if x == x_labels[0]:
                storedvals[x].append(load_values('store_hv/' + x + '_hv_ncycle' + str(n_cycle) + '_filter' + str(n_filter) + '_fevals' + str(max_fevals) + 'DTLZ' + str(problem_number) + '_run' + str(run+1) + '.txt'))
            else:
                storedvals[x].append(load_values('store_hv/' + x + '_hv_ncycle' + '_fevals' + str(max_fevals-1) + 'DTLZ' + str(problem_number) + '_run' + str(run+1) + '.txt'))                

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
    if x == x_labels[0]:
        x = 'RBFMopt'
    plot_spline(plt, fevals_plot, median_hv, max_fevals, x)


plt.legend(loc='best')
plt.title('RBFMopt, NSGA-II and MOEAD for DTLZ Test Problem Suite')
plt.xlabel('Function evaluations')
plt.ylabel('Median hypervolume over '+str(n)+' runs')
plt.grid()
plt.savefig(cwd + '/graphics/benchmark_graph_median_final' + '.png', dpi=300)

plt.clf()

plt.title('RBFMopt, NSGA-II and MOEAD for DTLZ Test Problem Suite')
plt.boxplot(boxplots)
plt.xticks([1, 2, 3], ['RBFMopt', 'MOEAD', 'NSGA-II'])
plt.savefig(cwd + '/graphics/benchmark_boxplot_median_final' + '.png', dpi=300)
