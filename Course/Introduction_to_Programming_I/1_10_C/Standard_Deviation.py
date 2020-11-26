import math
#標準偏差を計算して出力する関数
def Standard_Deviation(n,*args):
    sum = 0
    stdv = 0
    for arg in args:
        sum += arg
    m = sum / n
    for arg in args:
        stdv += (arg-m)**2
    stdv = stdv / n
    print("{}".format(math.sqrt(stdv)))

while True:
    n = int(input())
    if n==0:
        break
    s = [int(x) for x in input().split()]
    Standard_Deviation(n,*s)