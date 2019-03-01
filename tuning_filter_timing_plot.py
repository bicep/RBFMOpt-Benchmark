import matplotlib.pyplot as plt
import numpy as np
from utils.utils import load_values

n = 5
dim = 30
cycle = 3 
max_fevals = (dim+1) * 50

problem_plot = ["1", "2", "3", "4", "6"]
fig, ax = plt.subplots()


x_labels = [str(3*dim), str(6*dim), str(9*dim), str(None)]

storedvals = {
  str(3*dim): [],
  str(6*dim): [],
  str(9*dim): [],
  str(None): []
}

for i in range(6):
    problem_number = i+1

    if i == 4:
        continue

    for x in x_labels:
        for run in range(n):
            values = []
            values.append(load_values('timer/rbfmopt_timer_ncycle' + str(cycle) + '_filter' + x + '_fevals' + str(max_fevals) + '_' + 'ZDT' + str(problem_number) + '_run' + str(run+1)+'.txt'))
        storedvals[x].append(np.mean(values))

# calc the mean of the normalized values
for x in x_labels:
    ax.scatter(problem_plot, storedvals[x], label=x)


plt.legend(loc='best')
plt.title('Timing between 90, 180, 270 and no filter')
plt.xlabel('Problem number')
plt.ylabel('Mean timing over '+str(n)+' runs')
plt.grid()
plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Tuning_timing_graph' + '.png')

plt.clf()
