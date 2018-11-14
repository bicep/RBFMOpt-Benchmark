import numpy as numpy
from scipy.interpolate import UnivariateSpline

def plot_spline(plt, x_plot, y_plot, max_fevals, label):
    spline = UnivariateSpline(x_plot, y_plot, s=5)

    spline_x = numpy.linspace(0, max_fevals, 20)
    spline = spline(spline_x)
    plt.plot(spline_x, spline, label=label)

# Weighted Objective Function (Augmented Chebyshev)
def calculate_weighted_objective(weights, values, rho):
    weighted_vals = [value * weight for value, weight in zip(values,weights)] 
    aug_tcheby = max(weighted_vals) + rho * sum(weighted_vals)
    return aug_tcheby
