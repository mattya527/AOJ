cnt = 0
W = input()
while True:
    T = input().split()
    if T[0] == 'END_OF_TEXT' :
        break
    else :
        T=list(map(str.lower,T)) #すべての単語を小文字に変換
        cnt += T.count(W)

print(cnt)
