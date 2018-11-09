import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
import _thread
from timeit import default_timer as timer


start = timer()
if __name__ == '__main__':
    with Pool(5) as p:
        np.random.seed(444)
        np.set_printoptions(precision=3)
        d = np.random.laplace(loc=3000, scale=1, size=5000000)


        def f():
            hist, bin_edges = np.histogram(d)
            x = hist
            y = bin_edges
            return x, y


        n, bins, patches = plt.hist(x=d, bins='auto', color='#0504aa',
                                    alpha=0.7, rwidth=0.85)

        end = timer()
        print("1:: ", end - start)

        plt.show()



