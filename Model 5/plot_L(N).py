from libraries.IO import readData
from libraries.IO import saveData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW

a = 2
if a == 2:
    bin_no = 100
    start = 0
    end = 10000

    fixed_n = [0]


    for i, maxN in enumerate([0]):
        array = readData("inf_l_" + str(maxN))
        # array = list(map(lambda x: 10 ** x, array))
        med = np.median(array)
        std = np.std(array)
        title = 'median = {:10.2f}'.format(10 ** med)
        bins = np.linspace(-1, 10, bin_no)
        y, bins = np.histogram(array, bins=bins)
        y = y / max(y)
        plt.plot(bins[:-1], y,label='N={}'.format(maxN))
        print(title, 'min: {:3.0f}, max: {:10.0f}'.format(min(array), max(array)))
        plt.xlabel("Expected civilization longevity in log(years)")
        plt.ylabel("Relative probability")
        # ax.axes.get_yaxis().set_ticklabels(["Probability"])


    plt.show()
