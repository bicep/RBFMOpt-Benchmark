import sys
import pygmo as pg
from utils.pygmo_utils import calculate_mean_pyg, calculate_mean_rbf
from utils.utils import save_values

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 10
dim = 6
fdim = 2
problem_name = 'dtlz'
problem_number = 7
cycle = 3

# python benchmark_calc.py 10 6 2
if (len(sys.argv) > 0):
    n = int(sys.argv[1])
    dim = int(sys.argv[2])
    fdim = int(sys.argv[3])
    problem_name = (sys.argv[4])
    if (problem_name != 'dtlz' and problem_name != 'zdt'):
        raise Exception('Please choose between DTLZ or ZDT')
    if (problem_name == 'zdt'):
        problem_number = 6

max_fevals = (dim+1) * 2

# To account for the fact that the zero index array in util functions
# are actually the 1st feval
working_fevals = max_fevals-1
pop_size = 24
seed = 33

# For the each problem in the problem suite
for i in range(problem_number):
    problem_function = getattr(pg.problems, problem_name)
    if (problem_name == "dtlz"):
        problem = pg.problem(problem_function(i+1, dim=dim, fdim=fdim))
    else:
        problem = pg.problem(problem_function(i+1, param=dim))
    algo_moead = pg.algorithm(pg.moead(gen=1))
    algo_nsga2 = pg.algorithm(pg.nsga2(gen=1))

    # Hypervolume calculations, mean taken over n number of times
    hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, cycle)
    hv_moead_plot = calculate_mean_pyg(n, algo_moead, working_fevals, pop_size, seed, problem)
    hv_nsga2_plot = calculate_mean_pyg(n, algo_nsga2, working_fevals, pop_size, seed, problem)
    fevals_plot = range(0, max_fevals)

    save_values('storedvalues/rbfmopt_hv_' + problem.get_name() + '_fevals' + str(max_fevals) + '.txt', hv_rbfmopt_plot.tolist())
    save_values('storedvalues/moead_hv_' + problem.get_name() + '_fevals' + str(max_fevals) + '.txt', hv_moead_plot.tolist())
    save_values('storedvalues/nsga2_hv_' + problem.get_name() + '_fevals' + str(max_fevals) + '.txt', hv_nsga2_plot.tolist())
