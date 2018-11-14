import pygmo as pg
import matplotlib.pyplot as plt
from utils.pygmo_utils import calculate_mean_pyg, calculate_mean_rbf
from utils.utils import plot_spline

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 2
max_fevals = 30
# To account for the fact that the zero index array in util functions
# are actually the 1st feval
working_fevals = max_fevals-1
pop_size = 24
seed = 33

# For the 7 dtlz problems
for i in range(7):
    problem = pg.problem(pg.problems.dtlz(i+1, dim=6, fdim=2))
    # problem = pg.problem(pg.problems.dtlz(2, dim=6, fdim=2))
    algo_moead = pg.algorithm(pg.moead(gen=1))
    algo_nsga2 = pg.algorithm(pg.nsga2(gen=1))

    # Hypervolume calculations, mean taken over n number of times
    hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem)
    hv_moead_plot = calculate_mean_pyg(n, algo_moead, working_fevals, pop_size, seed, problem)
    hv_nsga2_plot = calculate_mean_pyg(n, algo_nsga2, working_fevals, pop_size, seed, problem)
    fevals_plot = range(0, max_fevals)

    fig, ax = plt.subplots()

    plot_spline(plt, fevals_plot, hv_rbfmopt_plot, max_fevals, "rbfmopt")
    plot_spline(plt, fevals_plot, hv_moead_plot, max_fevals, "moead")
    plot_spline(plt, fevals_plot, hv_nsga2_plot, max_fevals, "nsga2")

    plt.legend(loc='best')
    plt.title('DTLZ' + str(i+1))
    plt.xlabel('Function evaluations')
    plt.ylabel('Mean hypervolume over '+str(n)+' runs')
    plt.grid()
    plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Benchmark_Multi' + str(i+1) +'.png')
    plt.show()
