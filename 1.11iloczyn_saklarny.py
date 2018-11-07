
a = [1,2,12,4]
b = [2,4,2,8]
y = [0,0,0,0]
z = 0

for i in range (3):
    y[i] = a[i]*b[i]
    print(y[i])
for i in range (3):
    z +=y[i]
    print(z)
print("iloczyn skalarny wynosi: ",z)