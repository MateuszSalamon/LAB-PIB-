
# 3x3 matrix
a =  [[0 for x in range(2)] for y in range (2)]
# universal code for n * n matrix

def get_cofactor(a, temp,p,q,n):

    i = 0
    j = 0

    for row in range(n):
        for col in range(n):
            if (row!= p and col != q):
                j = j + 1
                temp[i][j] = a[row][col]

                if j==n-1:
                    j=0
                    i+=1




def determinant(a,n):

    det = 0

    if n == 1:
        return a[0][0]

    temp = [[0 for x in range(2)] for y in range (2)]
    sign = 1

    for i in range(n):
        get_cofactor(a,temp,0,i,n)
        det += sign * a[0][i] * determinant(temp,n-1)
        sign = -sign

    return det


