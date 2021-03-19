# PLOT 3:::  Scatter plot with linear regression line of best fit
    # Useful for:
    # This is a normal scatter plot but we also plot a simple
    # regression line to see the correlation between the x and the y variables.

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action="once")

class scatterPlotWithRegressionLine:
    def scatterPlotWithRegressionLine(self):
        path="datasets/mpg_ggplot2.csv"
        df=pd.read_csv(path)

        # Prepare the data for plotting
        # filter only 2 classes to separate it more easily on the plot
        df=df[df["cyl"].isin([4, 8])]
        # print("I m df", df)
        # Plot the data using seaborn
        sns.lmplot(x="displ", y= "hwy", data= df, hue="cyl")

        # Prettify the plot

        # Since we are using seaborn and this library uses matplotlib behind the scenes
        # u can call plt.gcs() (get current axes) and all the familiar matplotlib commands
        ax=plt.gca()

        # Change the upper limit of the plot to make it more pleasant
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 50)

        # set the title
        ax.set_title("Scatter plot with regression")
        plt.show()

