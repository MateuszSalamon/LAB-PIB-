
import random
from multiprocessing import Pool
from timeit import default_timer as timer

import numpy as np

if __name__ == '__main__':
    with Pool(5) as p:

        length = 70

        matr1 =  [[0 for x in range(length)] for y in range (length)]
        matr2 =  [[0 for x in range(length)] for y in range (length)]
        matr3 =  [[0 for x in range(length)] for y in range (length)]

        start = 0
        end = 7
        num = 1


        def rand(start, end, num):
            res = int

            for j in range(num):
                res = random.randint(start, end)  # print(res[j])

            return res



        # add random values to matrix1 and matrix2
        for i in range (length):
            for j in range(length):
                matr1[i][j] = rand(start, end, num)
                matr2[i][j] = rand(start, end, num)
                # print("_1","|",i, "|",j, "|",matr1[i][j])
                # print("_2","|",i, "|",j, "|",matr2[i][j])


        # nested matrix multiplication

        def matrix_mult_nest(a, b):
            zip_b = zip(*b)
            zip_b = list(zip_b)
            return [[sum(a*b for a, b in zip(row_a, col_b))
                     for col_b in zip_b] for row_a in a]


        t_nest = timer()  # start time for nested

        matr4 = matrix_mult_nest(matr1, matr2)

        elapsed_t_nest = timer()-t_nest  # elapsed time for nested

        # NUMPY
        # gives out incorrect output
        # matmul designed for 2D matrix


        print("nested", matr4)


        my = np.matrix(matr1)
        mx = np.matrix(matr2)

        t_numpy = timer() # start time measure for numpy

        m3 = np.matmul(mx, my)

        elapsed_t_numpy = timer()-t_numpy # elapsed time for numpy

        print("numpy", m3)

        # loop mult code

        t_for_loop = timer()  # start time for loops


        for i in range(length):
            for j in range(length):
                for k in range(length):
                    matr3[i][j] += matr1[i][k] * matr2[k][j]

        elapsed_t_for_loop = timer()-t_for_loop # elapsed time for for loop

        print("for loop", matr3)

        # print("matr1", matr1)
        # print("matr2", matr2)

        print("tnest", elapsed_t_nest)
        print("tnumpy", elapsed_t_numpy)
        print("tforloop", elapsed_t_for_loop)

