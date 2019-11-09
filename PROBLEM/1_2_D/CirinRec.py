l=input().split()
W=l[0]
H=l[1]
x=l[2]
y=l[3]
r=l[4]
f=0
if x+r>W:
    f=1
if y+r>H:
    f=1
if r>x:
    f=1
if r>y:
    f=1
if f==0:
    print("Yes")
else :
    print("No")
