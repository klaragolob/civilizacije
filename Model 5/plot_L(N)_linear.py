from libraries.IO import readData
from libraries.IO import saveData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from libraries.StandardizeDistribution import StandardizeDistributionW


if True:
    bin_no = 100
    start = 0
    end = 10000
    bins = np.linspace(start, end, bin_no)
    for i, maxN in enumerate([0]):
        array = readData("inf_l_" + str(maxN))
        array = list(map(lambda x: 10 ** x, array))
        med = np.median(array)
        std = np.std(array)
        title = 'median = {:8.0f}'.format(med)
        plt.title(title)
        bins = np.linspace(0, 10000, bin_no)
        y, bins = np.histogram(array, bins=bins)
        y = y / max(y)
        plt.plot(bins[:-1], y)
        print(title, 'min: {:3.0f}, max: {:10.0f}'.format(min(array), max(array)))
        plt.xlabel("Expected civilization longevity in years")
        plt.ylabel("Relative probability")

        
    plt.show()


