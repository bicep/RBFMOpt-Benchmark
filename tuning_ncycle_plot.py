import matplotlib.pyplot as plt
import numpy as np
from utils.utils import plot_spline, load_values, normalize

n = 10
dim = 30
max_fevals = (dim+1) * 50


fevals_plot = range(0, max_fevals)

all_hv_3 = []
all_hv_6 = []
all_hv_9 = []

# For the 4 zdt problems
for i in range(4):

    if i == 4:
        continue

    hv_cycle_3 = load_values('storedvalues/rbfmopt_hv_' + 'cycle' + str(3) + '_ZDT' + str(i+1) + '_fevals' + str(max_fevals) + '.txt')
    hv_cycle_6 = load_values('storedvalues/rbfmopt_hv_' + 'cycle' + str(6) + '_ZDT' + str(i+1) + '_fevals' + str(max_fevals) + '.txt')
    hv_cycle_9 = load_values('storedvalues/rbfmopt_hv_' + 'cycle' + str(9) + '_ZDT' + str(i+1) + '_fevals' + str(max_fevals) + '.txt')

    best_hv = max(max(hv_cycle_3), max(hv_cycle_6), max(hv_cycle_9))
    worst_hv = min(min(hv_cycle_3), min(hv_cycle_6), min(hv_cycle_9))

    if i == 0:
        all_hv_3 = [normalize(hv_cycle_3, best_hv, worst_hv)]
        all_hv_6 = [normalize(hv_cycle_6, best_hv, worst_hv)]
        all_hv_9 = [normalize(hv_cycle_9, best_hv, worst_hv)]
    else:
        all_hv_3 = np.vstack((all_hv_3, normalize(hv_cycle_3, best_hv, worst_hv)))
        all_hv_6 = np.vstack((all_hv_6, normalize(hv_cycle_6, best_hv, worst_hv)))
        all_hv_9 = np.vstack((all_hv_9, normalize(hv_cycle_9, best_hv, worst_hv)))


mean_hv_3 = np.mean(all_hv_3, axis=0)
mean_hv_6 = np.mean(all_hv_6, axis=0)
mean_hv_9 = np.mean(all_hv_9, axis=0)

fig, ax = plt.subplots()

plot_spline(plt, fevals_plot, mean_hv_3, max_fevals, "3 cycles")
plot_spline(plt, fevals_plot, mean_hv_6, max_fevals, "6 cycles")
plot_spline(plt, fevals_plot, mean_hv_9, max_fevals, "9 cycles")

plt.legend(loc='best')
plt.title('Tuning between 3, 6 and 9 cycles')
plt.xlabel('Function evaluations')
plt.ylabel('Mean hypervolume over '+str(n)+' runs')
plt.grid()
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Tuning_graph' + '.png')

plt.clf()

"""
data = [mean_hv_3, mean_hv_6, mean_hv_9]
plt.title('Tuning between 3, 6 and 9 cycles')
plt.boxplot(data)
plt.xticks([1, 2, 3], ['3 cycles', '6 cycles', '9 cycles'])
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Tuning_boxplot' + '.png')
"""