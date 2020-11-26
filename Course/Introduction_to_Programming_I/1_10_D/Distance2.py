import math

#ミンコフスキー距離を求める関数
def Minkowski(n,*args):
    #p = 1
    Dxy = 0
    for i in range(n):
        Dxy += abs(x[i] - y[i])
    print(float(Dxy))
    #p = 2
    Dxy = 0
    for i in range(n):
        Dxy += abs(x[i] - y[i])**2
    print(math.sqrt(Dxy))
    #p = 3
    Dxy = 0
    for i in range(n):
        Dxy += abs(x[i] - y[i])**3
    print(math.pow(Dxy,1/3))
    #p = ∞
    Dxy = 0
    for i in range(n):
        if Dxy < abs(x[i] - y[i]):
            Dxy = abs(x[i] - y[i])
    print(float(Dxy))
    
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
Minkowski(n,*x,*y)
