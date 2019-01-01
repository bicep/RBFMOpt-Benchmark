import pygmo as pg
from utils.pygmo_utils import calculate_mean_rbf
from utils.utils import gen_csv

# where n is the number of times the meta-heuristic algorithms are run to get the mean
n = 1
problem_name = 'zdt'
problem_number = 6

# To account for the fact that the zero index array in util functions
# are actually the 1st feval
pop_size = 24
seed = 33
default_rf = 3

# i is the problem number chosen
i = 4
dim = 30
problem_function = getattr(pg.problems, problem_name)
problem = pg.problem(problem_function(i, param=dim))

max_fevals = 110

working_fevals = max_fevals-1

file_string = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem' + str(i) + '_dvar' + str(dim) + '.txt'
stream = open(file_string, 'a')
hv_rbfmopt_plot = calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, default_rf, output_stream=stream)
stream.close()

csv_file_string = '/Users/rogerko/dev/Opossum/benchmark/csv/benchmark_problem' + str(i) + '_dvar' + str(dim) + '.csv'

# load the txt file and gen csv
gen_csv(file_string, csv_file_string)
