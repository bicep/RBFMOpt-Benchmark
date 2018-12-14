import json as json
import numpy as numpy
from scipy.interpolate import make_interp_spline


def plot_spline(plt, x_plot, y_plot, max_fevals, label):
    # spline = CubicSpline(x_plot, y_plot)

    spline_x = numpy.linspace(0, max_fevals, 20)

    spl = make_interp_spline(x_plot, y_plot, k=3)  # BSpline object
    power_smooth = spl(spline_x)

    plt.plot(spline_x, power_smooth, label=label)


# Weighted Objective Function (Augmented Chebyshev)
def calculate_weighted_objective(weights, values, rho):
    weighted_vals = [value * weight for value, weight in zip(values, weights)] 
    aug_tcheby = max(weighted_vals) + rho * sum(weighted_vals)
    return aug_tcheby


def save_values(dir, values):
    with open(dir, 'w') as filehandle:
        json.dump(values, filehandle)


def load_values(dir):
    with open(dir, 'r') as filehandle:  
        return json.load(filehandle)
