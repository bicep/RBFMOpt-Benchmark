import pygmo as pg
from utils.pygmo_utils import calculate_mean_rbf
from utils.utils import save_values

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 1
dim = 30
problem_name = 'zdt'
problem_number = 6

max_fevals = (dim+1) * 50

# To account for the fact that the zero index array in util functions
# are actually the 1st feval
working_fevals = max_fevals-1
pop_size = 24
seed = 33

default_rf = 3
max_filter = 3

# For the each problem in the problem suite
for i in range(problem_number):
    if i == 4:
        break

    problem_function = getattr(pg.problems, problem_name)

    problem = pg.problem(problem_function(i+1, param=dim))

    hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, default_rf, max_filter=None)
    save_values('store_hv/rbfmopt_hv_cycle' + str(default_rf) + '_' + problem.get_name() + '_fevals' + str(max_fevals) + '.txt', hv_rbfmopt_plot.tolist())

    for j in range(3):
        hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, default_rf, (j+1)*max_filter*dim)
        save_values('store_hv/rbfmopt_hv_cycle' + str(default_rf) + '_' + problem.get_name() + '_fevals' + str(max_fevals) + '.txt', hv_rbfmopt_plot.tolist())
    
