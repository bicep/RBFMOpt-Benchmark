import matplotlib.pyplot as plt
from utils.utils import plot_spline, load_values

n = 10
max_fevals = 100  # (dim+1) * 100

fevals_plot = range(0, max_fevals)

# For the 7 dtlz problems
for i in range(7):

    hv_rbfmopt_plot = load_values('store_hv/rbfmopt_hv_' + 'dtlz' + str(i+1) + '_fevals' + str(max_fevals) + '.txt')
    hv_moead_plot = load_values('store_hv/moead_hv_' + 'dtlz' + str(i+1) + '_fevals' + str(max_fevals) + '.txt')
    hv_nsga2_plot = load_values('store_hv/nsga2_hv_' + 'dtlz' + str(i+1) + '_fevals' + str(max_fevals) + '.txt')

    fig, ax = plt.subplots()

    plot_spline(plt, fevals_plot, hv_rbfmopt_plot, max_fevals, "rbfmopt")
    plot_spline(plt, fevals_plot, hv_moead_plot, max_fevals, "moead")
    plot_spline(plt, fevals_plot, hv_nsga2_plot, max_fevals, "nsga2")

    plt.legend(loc='best')
    plt.title('DTLZ' + str(i+1))
    plt.xlabel('Function evaluations')
    plt.ylabel('Mean hypervolume over '+str(n)+' runs')
    plt.grid()
    plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Graph_DTLZ' + str(i+1) + '.png')

    plt.clf()

    data = [hv_rbfmopt_plot, hv_moead_plot, hv_nsga2_plot]
    plt.title('DTLZ' + str(i+1))
    plt.boxplot(data)
    plt.xticks([1, 2, 3], ['RBFMopt', 'MOEAD', 'NSGAII'])
    plt.savefig('/Users/rogerko/dev/Opossum/benchmark/graphics/Boxplot_DTLZ' + str(i+1) + '.png')