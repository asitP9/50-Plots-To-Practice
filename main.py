#Scatteplot is a classic and fundamental plot used to study the relationship between two variables.
# If you have multiple groups in your data you may want to visualise each group in a different color.
# In matplotlib, you can conveniently do this using plt.scatterplot().


# https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/#1.-Scatter-plot
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action="once")

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

# PLOT 1:::
def scatterPlot():
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


# PLOT 2:::
def bubblePlot():
    from matplotlib import patches
    from scipy.spatial import ConvexHull
    import warnings; warnings.simplefilter('ignore')
    sns.set_style("white")

    # Step 1: Prepare Data
    midwest=pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/midwest_filter.csv")

    # As many colors as there are unique midwest['category']
    categories=np.unique(midwest['category'])
    colors=[plt.cm.tab10(i/float(len(categories)-1)) for i in range(len(categories))]

    # Step 2: Draw Scatter Plot with unique color for each category
    fig=plt.figure(figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')

    for i, category in enumerate(categories):
        plt.scatter('area', 'poptotal',
                    data=midwest.loc[midwest.category==category, :],
                    s=20, c=colors[i], label=str(category))

    # Step 3: Encircling
    # https://stackoverflow.com/questions/44575681/how-do-i-encircle-different-data-sets-in-scatter-plot
    def encircle(x, y, ax=None, **kw):
        if not ax: ax=plt.gca()
        p=np.c_[x, y]
        hull=ConvexHull(p)
        poly=plt.Polygon(p[hull.vertices, :], **kw)
        ax.add_patch(poly)

    # Select data to be encircled
    midwest_encircle_data=midwest.loc[midwest.state=='IN', :]

    # Draw Polygon surrounding Vertices
    encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="k", fc="gold", alpha=0.1)
    encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="firebrick", fc="none", linewidth=1.5)

    # Decorations
    plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000), xlabel='Area', ylabel="Population")

    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title("Bubble Plot with encircling", fontsize=22)
    plt.legend(fontsize=12)
    plt.show()



    # PLOT 3:::  Scatter plot with linear regression line of best fit
    # Useful for:
    # This is a normal scatter plot but we also plot a simple
    # regression line to see the correlation between the x and the y variables.
def scatterPlotWithRegressionLine():
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



# Plot 4: Jittering with Strip Plot
# Useful for
# Draw a scatterplot where one variable is categorical.
# This is useful to see the distributions of the points of each category.
def jitteringWithStripPlot():
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jitteringWithStripPlot()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
