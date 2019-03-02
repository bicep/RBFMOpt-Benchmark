import json as json
import csv
import numpy as numpy
from scipy.interpolate import make_interp_spline

def gen_csv(filename, csvfilename):
    with open(filename) as f:
        # open the csv file
        csvf = open(csvfilename, 'a')
        # add the variables to the csvfile
        n_run = 0
        csvf.write("nrun,iter,cycle,action,obj_value,time,gap\n")
        for line in f:
            # strip the front and end spacing
            line = line.lstrip()
            # If contains iter then increase the count
            if "Iter" in line:
                n_run += 1
                continue
            if "Summary" in line:
                continue
            # Get rid of the ---- (break)
            if "----" in line:
                continue
            # Replace the white spaces with a comma
            # re.sub(' +', ' ', line)
            csvf.write(str(n_run) + ',')
            csvf.write(" ".join(line.split()).replace(' ', ',').replace('*', ''))
            csvf.write('\n')
        csvf.close()
        f.close()


def calc_local_step_perfeval(filename):
    ave = []
    with open(filename, newline='\n') as csvf:
        reader = csv.DictReader(csvf)
        local = 0
        prev_time = 0
        fevals = 0
        for row in reader:
            if row['action'] == 'LocalStep':
                local = (float(row['time']) - prev_time)
            if row['action'] != 'Initialization':
                fevals += 1
                ave.append(local)
            prev_time = float(row['time'])
        csvf.close()
    return ave


def plot_spline(plt, x_plot, y_plot, max_fevals, label, start=0):
    # spline = CubicSpline(x_plot, y_plot)

    spline_x = numpy.linspace(start, max_fevals, 20)

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

def normalize_helper(x, best, worst):
    return ((x-worst)/(best-worst))

def normalize(arr, best, worst):
    return [normalize_helper(x, best, worst) for x in arr]
