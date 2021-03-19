# PLOT 1:::
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action="once")

class scatterPlot:

    def scatterPlot(self):
        # Import Dataset
        midwest=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

        # Prepare Data
        # Create as many colors as there are unique midwest['category']
        categories=np.unique(midwest['category'])
        colors=[plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]
        print("COOLORS=:::", colors)
        # Draw plot from each category
        plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

        for i, category in enumerate(categories):
            plt.scatter('area', 'poptotal',
                        data=midwest.loc[midwest.category==category, :],
                        s=20, c=colors[i], label=str(category))

        # Decorations
        plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000), xlabel='Area', ylabel="Population")

        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.title("Scatter plot of Midwest Area Vs Population", fontsize=22)
        plt.legend(fontsize=12)
        plt.show()