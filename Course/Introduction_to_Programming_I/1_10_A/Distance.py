import math

xy = input().split()
x1 = float(xy[0])
y1 = float(xy[1])
x2 = float(xy[2])
y2 = float(xy[3])

x = x2-x1
y = y2-y1
dist = math.sqrt(x**2+y**2)
print(dist)