# Tuning and Benchmarking a RBFMopt

This repository contains code that was used to tune and benchmark RBFMopt for my Yale-NUS Computer Science Capstone Project.

**Crucially, RBFMopt was shown to outperform genetic algorithms like MOEAD and NSGA-II using the DTLZ test problem suite.**

![graph 1](/graphics/benchmark_graph_median.png)
![boxplot 1](/graphics/benchmark_boxplot_median.png)

All the tuning results and plots can be found in the graphics folder of this repo.

----
## What is RBFMopt?
RBFMopt is a multi-objective blackbox optimization algorithm conceived of by [Dr Thomas Wortmann](https://www.researchgate.net/profile/Thomas_Wortmann) and based off the single-objective [RBFOpt](https://github.com/coin-or/rbfopt) designed by Dr Giacomo Nannicini. 

The initial RBFMopt was implemented by Dr Wortmann in C#. I rewrote the code in Python and extended it to be able to filter points it was refeeding into the algorithm. More details can be found in a private repository. Please email Dr Wortmann if you are interested.

----
## Setup
1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)- you need this to install Pygmo (which gives us access to NSGA II, MOEAD, and test problems)
2. Create a virtual env with Python 3.6 using `conda create -n benchmark python=3.6`
3. Activate the virtual env `source activate benchmark`
4. `pip install requirements.txt`- this installs necessary packages like RBFOpt
5. `git clone` the private RBFMopt repository (again please request access)
6. While in the conda virtual env and in the RBFMopt directory, install `pip install -e .`

## Steps to repeat tuning findings
1. Activate the virtual env `source activate benchmark`
2. First do the calculations `python tuning_filter_calc.py` and `python tuning_ncycle_calc.py`. Each will calculate various hypervolume values of the pareto front solution to the ZDT problem test suite for the RBFMopt aglgorithm of varying filter values (90, 180, 270 and No filter in the case of tuning_filter_calc.py) and ncycle values (3, 6 and 9 in the case of tuning_ncycle_calc.py).
3. Once the calculations are done plot the graphs and boxplots with `python tuning_filter_plot.py` and `python tuning_ncycle_plot.py`.

## Steps to repeat benchmarking findings
1. Activate the virtual env `source activate benchmark`
2. First do the calculations `python benchmark_calc.py`. Each will calculate various hypervolume values of the pareto front solution to the DTLZ problem test suite for RBFMopt(filter=270, ncycle=9), NSGAII and MOEAD .
3. Once the calculations are done plot the graphs and boxplots with `python benchmark_plot.py`.

----
## 