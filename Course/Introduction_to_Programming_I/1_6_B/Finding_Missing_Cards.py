#４ｘ１３の空のリストの作成
cards = [[False for i in range(13)] for j in range(4)]

n = int(input())#足りない数の入力
for i in range(n):
    ch,rank = input().split()
    rank = int(rank)
    if ch == 'S':
        cards[0][rank-1] = True
    elif ch == 'H':
        cards[1][rank-1] = True
    elif ch == 'C':
        cards[2][rank-1] = True
    elif ch == 'D':
        cards[3][rank-1] = True

for i in range(4):
    for j in range(13):
        if cards[i][j]  == False:
            if i == 0:
                print('S',j+1)
            elif i == 1:
                print('H',j+1)
            elif i == 2:
                print('C',j+1)
            elif i == 3:
                print('D',j+1)
