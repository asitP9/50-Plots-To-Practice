# Plot 4: Jittering with Strip Plot
# Useful for
# Draw a scatterplot where one variable is categorical.
# This is useful to see the distributions of the points of each category.
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action="once")

class jitteringWithStripPlot:
    def jitteringWithStripPlot(self):
        path="datasets/mpg_ggplot2.csv"
        df=pd.read_csv(path)


        # Prepare the data for plotting
        # Separate X and Y variables
        x=df["cty"]
        y=df["hwy"]


        # Instanciate the figure
        plt.figure(figsize=(10, 7))

        # Plot the data using Seaborn
        ax=sns.stripplot(x=x, y=y)

        # Prettify the plot
        # set title
        ax=ax.set_title("Jitter Plot")
        plt.show()


