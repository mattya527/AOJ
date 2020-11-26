while(True):
    w = input() #文字列の入力
    if w == '-':
        break
    m = int(input()) #シャッフル回数の入力
    for i in range(m):
        h = int(input()) #入れ替える文字列の数を入力
        front = w[0:h]
        back = w[h:]
        w = back+front
    print(w)
