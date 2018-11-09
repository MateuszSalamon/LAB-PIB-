import  numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

start2 = timer()

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

end2 = timer()
print("2::", end2-start2)
plt.show()

