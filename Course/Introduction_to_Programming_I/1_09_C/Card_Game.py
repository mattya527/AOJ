n = int(input()) #カードの枚数の入力
xcnt = ycnt = 0

for i in range(n):
    x,y = input().split() 
    if x > y :
        xcnt += 3
    elif x < y:
        ycnt += 3
    else:
        xcnt += 1
        ycnt += 1

print("{} {}".format(xcnt,ycnt))
