#
# generate map function
#

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


def gen_map(data, route):
    fig = plt.figure()
    ax  = plt.axes()

    allspot  = [[data.iat[i,1] for i in range(len(data))], [data.iat[i,2] for i in range(len(data))]]
    label    = [data.iat[i,0] for i in range(len(data))]

    plotlist = [[data.iat[i[0],1] for i in route], [data.iat[i[0],2] for i in route]]
    
    ax.scatter(allspot[1], allspot[0], marker="o")
    ax.plot(plotlist[1], plotlist[0], "o-", color="#00aa00")

    for i, L in enumerate(label):
        ax.annotate(L, xy=(allspot[1][i]+0.05, allspot[0][i]), size=5)

    clearance = 0.0005
    ax.set_xlim([min(allspot[1])-clearance, max(allspot[1])+clearance])
    ax.set_ylim([min(allspot[0])-clearance, max(allspot[0])+clearance])

    plt.savefig("output.png")


