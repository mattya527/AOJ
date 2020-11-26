import math
a,b,c = [int(x) for x in input().split()]
# a = 86
# b = 77
# c = 120

S = a * b * math.sin(math.radians(c)) / 2
print(S)

#余弦定理で2辺とその間の角からもう一つの辺を求める
#cosA = b^2+c^2-a^2 / 2bc
cosC = math.cos(math.radians(c))
# print(cosC)
x = (a**2+b**2)-2*b*a*cosC
x = math.sqrt(x)
# print(x)
print(a+b+x)

#aを底辺としたときの高さを求める
if c == 90:
    print(float(b))
else :
    h = b * math.sin(math.radians(c))
    print(h)