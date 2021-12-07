import matplotlib.pyplot as plt
import numpy as np

corr = [0.03807615691813725, 0.17009630107846674,
        0.130270606128409, 0.23892345579536003, -0.07395633196591865]


def createGraph(title, labelX, labelY, data):
    # x axis values
    x = np.arange(len(data))
    # corresponding y axis values
    y = data

    # plotting the points
    plt.plot(x, y, marker='o', linestyle='dashed')

    # naming the x axis
    plt.xlabel(labelX)
    # naming the y axis
    plt.ylabel(labelY)

    # giving a title to my graph
    plt.title(title)

    # function to show the plot
    plt.show()
