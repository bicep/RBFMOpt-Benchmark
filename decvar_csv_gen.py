import pygmo as pg
from utils.pygmo_utils import calc_and_gen_csv

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 1
problem_name = 'zdt'

# To account for the fact that the zero index array in util functions
# are actually the 1st feval
pop_size = 24
seed = 33
default_rf = 3

# i is the problem number chosen
i = 4
dim = 30
dim2 = 10
problem_function = getattr(pg.problems, problem_name)

max_fevals = 202

calc_and_gen_csv(problem_function, n, i, dim, max_fevals, default_rf)
calc_and_gen_csv(problem_function, n, i, dim2, max_fevals, default_rf)
