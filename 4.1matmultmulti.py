import random
from multiprocessing import Pool


if __name__ == '__main__':
    with Pool(5) as p:
        length = 50

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



        for i in range(length):
            for j in range(length):
                for k in range(length):
                    matr3[i][j] += matr1[i][k] * matr2[k][j]