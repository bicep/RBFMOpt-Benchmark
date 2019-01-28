import sys
import pygmo as pg
from utils.pygmo_utils import calculate_mean_rbf
from utils.utils import save_values
from problem.dtlz4 import dtlz4
from rbfmopt.PygmoUDP import PygmoUDP
import numpy as np

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 1
dim = 30
fdim = 2
problem_name = 'dtlz'
problem_number = 4
cycle = 3

max_fevals = 200

# To account for the fact that the zero index array in util functions
# are actually the 1st feval
working_fevals = max_fevals-1
pop_size = 24
seed = 33

# For the each problem in the problem suite
# problem_function = getattr(pg.problems, problem_name)

# problem = pg.problem(problem_function(problem_number, dim=dim, fdim=fdim))

udp = PygmoUDP(dim, np.array([-10] * dim), np.array([10] * dim), ['R'], fdim, dtlz4)

problem = pg.problem(udp)

# Hypervolume calculations, mean taken over n number of times
hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, cycle)
