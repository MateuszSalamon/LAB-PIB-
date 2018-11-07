import math

print("for function y = a*x^2+b*x+c")
print("input a: ")
a = int(input())
print("input b: ")
b = int(input())
print("input c: ")
c = int(input())

delta = (b*b)-(4*a*c)

if delta > 0:
    x1 = (-b +(delta)**(1/2)) / (2 * a)
    x2 = (-b -(delta)**(1/2)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif delta == 0:
    x1 = (-b)/(2 * a)
    print("x = ", x1)
else:
    print("No real numbers")

