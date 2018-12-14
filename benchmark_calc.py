import sys
import pygmo as pg
from utils.pygmo_utils import calculate_mean_pyg, calculate_mean_rbf
from utils.utils import save_values

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 10
dim = 6
fdim = 2

# python benchmark_calc.py 10 6 2
if (len(sys.argv) > 0):
    n = int(sys.argv[1])
    dim = int(sys.argv[2])
    fdim = int(sys.argv[3])

max_fevals = (dim+1) * 100

# To account for the fact that the zero index array in util functions
# are actually the 1st feval
working_fevals = max_fevals-1
pop_size = 24
seed = 33

# For the 7 dtlz problems
for i in range(7):
    problem = pg.problem(pg.problems.dtlz(i+1, dim=dim, fdim=fdim))
    # problem = pg.problem(pg.problems.dtlz(2, dim=6, fdim=2))
    algo_moead = pg.algorithm(pg.moead(gen=1))
    algo_nsga2 = pg.algorithm(pg.nsga2(gen=1))

    # Hypervolume calculations, mean taken over n number of times
    hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, (i+1))
    hv_moead_plot = calculate_mean_pyg(n, algo_moead, working_fevals, pop_size, seed, problem, (i+1))
    hv_nsga2_plot = calculate_mean_pyg(n, algo_nsga2, working_fevals, pop_size, seed, problem, (i+1))
    fevals_plot = range(0, max_fevals)

    save_values('storedvalues/rbfmopt_hv_dtlz' + str(i+1) + '_fevals' + str(max_fevals) + '.txt', hv_rbfmopt_plot.tolist())
    save_values('storedvalues/moead_hv_dtlz' + str(i+1) + '_fevals' + str(max_fevals) + '.txt', hv_moead_plot.tolist())
    save_values('storedvalues/nsga2_hv_dtlz' + str(i+1) + '_fevals' + str(max_fevals) + '.txt', hv_nsga2_plot.tolist())
