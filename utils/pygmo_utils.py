import numpy as np
import pygmo as pg
import math as math
import numpy as numpy
from classes.RbfmoptWrapper import RbfmoptWrapper
from utils.utils import save_values


# Calculates the hypervolume with a changing ref point
def reconstruct_hv_per_feval(max_fevals, x_list, f_list, hv_pop):
    # Have the same ref point at the beginning, and compute the starting hypervolume
    hv = [0]

    for fevals in range(max_fevals):
        hv_pop.push_back(x_list[fevals], f_list[fevals])
        new_hv = pg.hypervolume(hv_pop)
        ref = new_hv.refpoint(offset=4.0)
        hv.append(new_hv.compute(ref))

    return hv


# Calculates the hypervolume with all the old points from the old generations
# But starts with a full population. Used for the meta-heuristic algorithms
def reconstruct_hv_per_feval_meta(max_fevals, x_list, f_list, hv_pop):
    # Have the same ref point at the beginning, and compute the starting hypervolume
    original_hv = pg.hypervolume(hv_pop)
    ref = original_hv.refpoint(offset=4.0)
    hv = []

    for fevals in range(max_fevals):
        hv_pop.push_back(x_list[fevals], f_list[fevals])
        new_hv = pg.hypervolume(hv_pop)
        hv.append(new_hv.compute(ref))

    return hv


# Only for the evolutionary algos
# Stores the f and x values for each generation of the evolutionary algo,
# Then calculate the hypervolume per function evaluation
def get_hv_for_algo(algo, max_fevals, pop_size, seed, problem, nproblem):

    max_gen = math.ceil(max_fevals/pop_size)

    # same (random) starting population for both algos
    pop = pg.population(problem, pop_size, seed)

    f_list, x_list = pop.get_f(), pop.get_x()

    for i in range(max_gen):
        pop = algo.evolve(pop)

        # Get all the f and x values for this generation
        f_list = numpy.concatenate((f_list, pop.get_f()))
        x_list = numpy.concatenate((x_list, pop.get_x()))

    save_values('storedvalues/' + algo.get_name().split(':')[0] + '_x_dtlz' + str(nproblem) + '_run' + str(i+1) + '.txt', x_list.tolist())
    save_values('storedvalues/' + algo.get_name().split(':')[0] + '_f_dtlz' + str(nproblem) + '_run' + str(i+1) + '.txt', f_list.tolist())

    pop_empty = pg.population(prob=problem, seed=seed)

    return reconstruct_hv_per_feval(max_fevals, x_list, f_list, pop_empty)


# Meta-heuristic algorithms are stochastic and need to be run many times.
# Calculates the hypervolume n times, and then gets the mean across columns
# to give a 1D mean array
def calculate_mean_pyg(n, algo, max_fevals, pop_size, seed, problem, nproblem):

    # 2D array whose elements are the n arrays of hypervolume
    return_array = []
    for i in range(n):
        return_array.append(get_hv_for_algo(algo, max_fevals, pop_size, seed, problem, nproblem))
        # Make sure we change the seed each time the algo is being run
        seed += (i+1)
    return numpy.mean(return_array, axis=0)


# nproblem is the dtlz number
def calculate_mean_rbf(n, max_fevals, working_fevals, seed, problem, nproblem):
    return_array = []

    for i in range(n):
        # Create dictionary for algo settings
        dict_settings = {
            'max_evaluations': max_fevals,
            'rand_seed': seed,
        }
        algo_rbfmopt = RbfmoptWrapper(dict_settings, problem)

        # RBFMopt hypervolume calculations
        algo_rbfmopt.evolve()
        empty_pop = pg.population(prob=problem, seed=seed)

        x_list = np.array(algo_rbfmopt.get_x_list())
        f_list = np.array(algo_rbfmopt.get_f_list())

        save_values('storedvalues/rbfmopt_x_dtlz' + str(nproblem) + '_run' + str(i+1) + '.txt', x_list.tolist())
        save_values('storedvalues/rbfmopt_f_dtlz' + str(nproblem) + '_run' + str(i+1) + '.txt', f_list.tolist())

        return_array.append(reconstruct_hv_per_feval(working_fevals, algo_rbfmopt.get_x_list(), algo_rbfmopt.get_f_list(), empty_pop))

        # Make sure we change the seed each time the algo is being run
        seed += (i+1)

    return numpy.mean(return_array, axis=0)
