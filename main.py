#Scatteplot is a classic and fundamental plot used to study the relationship between two variables.
# If you have multiple groups in your data you may want to visualise each group in a different color.
# In matplotlib, you can conveniently do this using plt.scatterplot().

# https://www.kaggle.com/ra4bht/plotting-with-python-learn-80-plots-mod-ra
# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#1.-Scatter-plot
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action="once")


from scatterPlot import scatterPlot
from bubblePlot import bubblePlot
from scatterPlotWithRegressionLine import scatterPlotWithRegressionLine
from jitteringWithStripPlot import jitteringWithStripPlot
from countsPlot import countsPlot
from marginalHistogram import marginalHistogram


large=22; med=16; small=12

params={
    'axes.titlesize': large,
    'legend.fontsize': med,
    'figure.figsize': (16, 10),
    'axes.labelsize': med,
    'axes.titlesize': med,
    'xtick.labelsize': med,
    'ytick.labelsize': large
}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")


if __name__ == '__main__':
    # plot=bubblePlot()
    # plot.bubblePlot()

# PLOT 6
    plot=marginalHistogram()
    plot.marginalHistogram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
