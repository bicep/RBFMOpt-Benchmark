import math
import matplotlib.pyplot as plt
import numpy as np
from utils.utils import plot_spline, load_values, normalize

n = 5
dim = 30
cycle = 3 
max_fevals = (dim+1) * 50

fevals_plot = range(0, max_fevals)
fig, ax = plt.subplots()

x_labels = [str(3*dim), str(6*dim), str(9*dim), str(None)]

storedvals = {
  str(3*dim): [],
  str(6*dim): [],
  str(9*dim): [],
  str(None): []
}

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
        storedvals[x].append(load_values('store_hv/rbfmopt_hv_ncycle' + str(cycle) + '_filter' + x + '_fevals' + str(max_fevals) + 'ZDT' + str(problem_number) + '.txt'))

        # i is the (problem_number -1), get the max and min for the problem
        maxi = max(max(storedvals[x][i]), maxi)
        mini = min(min(storedvals[x][i]), mini)

    for x in x_labels:
        # normalize and replace original values
        storedvals[x][i] = normalize(storedvals[x][i], maxi, mini)

# calc the mean of the normalized values
for x in x_labels:
    mean_hv = np.mean(storedvals[x], axis=0)
    plot_spline(plt, fevals_plot, mean_hv, max_fevals, x)

plt.legend(loc='best')
plt.title('Tuning between 90, 180, 270 and no filter')
plt.xlabel('Function evaluations')
plt.ylabel('Mean hypervolume over '+str(n)+' runs')
plt.grid()
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Tuning_filter_graph' + '.png')

plt.clf()
