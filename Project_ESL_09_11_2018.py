import random
from myhdl import *


length = 16
start = 0
end = 50
num = 1


def rand(start,end,num):
    res = int

    for j in range(num):
        res = random.randint(start, end)  # print(res[j])

    return res

A = [0 for x in range(length)]
B = [0 for x in range(length)]
C = [0 for x in range(length)]


for i in range(length):
    C[i] += A[i]*B[i]


@block
def vector_mult():

    A1 = Signal(intbv(4)[128:])
    B1 = Signal(intbv(3)[128:])
    C1 = Signal(intbv(0)[128:])
    clk = Signal(bool(0))
    reset = Signal(bool(0))

    @always(delay(1))
    def vector_mult_hdl():
        for n in range(16):
            C1.next = A1*B1
            print( "%s zzz", C1)
    return vector_mult_hdl


inst = vector_mult()
inst.run_sim(30)



