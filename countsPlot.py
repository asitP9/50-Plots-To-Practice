import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action="once")

# PLOT 5: Counts Plot
# Useful for:
# Draw a scatterplot where one variable is categorical.
# In this plot we calculate the size of overlapping points in each category and for each y.
# This way, the bigger the bubble the more concentration we have in that region.

# More info:
# https://seaborn.pydata.org/generated/seaborn.stripplot.html

class countsPlot:
    def countsPlot(self):
        path="datasets/mpg_ggplot2.csv"
        df=pd.read_csv(path)

        # we need to make a groupby by variables of interest
        gb_df=df.groupby(["cty", "hwy"]).size().reset_index(name="counts")

        # sort the values
        gb_df.sort_values(["cty", "hwy", "counts"], ascending=True, inplace=True)

        # create a color for each group.
        # there are several way os doing, you can also use this line:
        # colors = [plt.cm.gist_earth(i/float(len(gb_df["cty"].unique()))) for i in range(len(gb_df["cty"].unique()))]
        colors={i:np.random.random(3,) for i in sorted(list(gb_df["cty"].unique()))}

        # instanciate the figure
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot()

        # iterate over each category and plot the data. This way, every group has it's own color and sizwe.
        # instantiate the figure
        for i in sorted(list(gb_df["cty"].unique())):
            # get x and y values for each group
            x_values = gb_df[gb_df['cty'] == i]["cty"]
            y_values = gb_df[gb_df['cty'] == i]["hwy"]
            print("my y values ", gb_df[gb_df['cty'] == i]["hwy"])
            # extract the size of each group to plot
            size = gb_df[gb_df["cty"] == i]["counts"]

            # extract the color for each group and covert it from rgb to hex
            color = mpl.colors.to_hex(colors[i])
            ax.scatter(x_values, y_values, s=size * 10, c=color)


        # prettify the plot
        ax.set_title("count_plot")
        plt.show()
