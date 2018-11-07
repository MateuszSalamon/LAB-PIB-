import random

matr1 =  [[0 for x in range(127)] for y in range (127)]
matr2 =  [[0 for x in range(127)] for y in range (127)]
matr3 =  [[0 for x in range(127)] for y in range (127)]


def rand(start,end,num):
    res = int

    for j in range(num):
        res = random.randint(start, end)  # print(res[j])

    return res


start = 0
end = 50
num = 1


for i in range (127):
    for j in range(127):
        matr1[i][j] = rand(start, end, num)
        matr2[i][j] = 2
        matr3[i][j] = matr1[i][j] + matr2[i][j]
        print("matrix 1 ", matr1[i][j])
        # print("matrix 3 ", matr3[i][j])

for i in range (127):
    for j in range(127):
        print("matrix 3 ", matr3[i][j])