import numpy
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
#np.random.seed(19680801)

def mat_draw(list1,str):
    x = numpy.array(list1)
    x_sorted = numpy.sort(x)

    n, bins, patches = plt.hist(x, 100000, density=True, facecolor='g', alpha=0.75)

    plt.xlabel('Sojourn time')
    plt.ylabel('Probability')
    plt.title('Distribution of %s queue sojourn time' % str)
    plt.xlim(0, 120)
    #percentiles to draw on x
    perc1 = x_sorted[9000000]
    perc2 = x_sorted[9500000]
    perc3 = x_sorted[9900000]
    plt.xticks([perc1,perc2,perc3],fontsize=4)
    plt.ylim(0, 0.1)
    plt.grid(True)
    plt.show()
