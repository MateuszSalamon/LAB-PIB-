import random

matr1 =  [[0 for x in range(7)] for y in range (7)]
matr2 =  [[0 for x in range(7)] for y in range (7)]
matr3 =  [[0 for x in range(7)] for y in range (7)]


def rand(start,end,num):
    res = int

    for j in range(num):
        res = random.randint(start, end)  # print(res[j])

    return res


start = 0
end = 7
num = 1


for i in range (7):
    for j in range(7):
        matr1[i][j] = rand(start, end, num)
        matr2[i][j] = rand(start, end, num)
        # print("_1","|",i, "|",j, "|",matr1[i][j])
        # print("_2","|",i, "|",j, "|",matr2[i][j])

for i in range(7):
    for j in range(7):

        for k in range(7):
            matr3[i][j] += matr1[i][k] * matr2[k][j]

        print("_3", "|", i, "|", j, "|", matr3[i][j])



