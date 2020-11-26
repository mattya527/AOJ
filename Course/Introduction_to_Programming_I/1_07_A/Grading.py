while True:
    #m,f,rの入力
    m,f,r = map(int,input().split())
    #試験を受けてないとき-1を入力
    #m,f,rがそれぞれ-1のとき終了
    if m == -1 and f == -1 and r == -1:
        break
    #中間試験、期末試験のいずれかを欠席した場合成績は F。
    if m == -1 or f == -1:
        print("F")
    # 中間試験と期末試験の合計点数が 80 以上ならば成績は A 。
    elif (m + f) >= 80:
        print("A")
    # 中間試験と期末試験の合計点数が 65 以上 80 未満ならば成績は B。
    elif (m + f) >=65 and (m + f) <80:
        print("B")
    # 中間試験と期末試験の合計点数が 50 以上 65 未満ならば成績は C。
    elif (m + f) >= 50 and (m + f) < 65:
        print("C")
    # 中間試験と期末試験の合計点数が 30 以上 50 未満ならば成績は D。 ただし、再試験の点数が 50 以上ならば成績は C。
    elif (m + f) >= 30 and (m + f) < 50 and r <50:
        print("D")
    elif (m + f) >= 30 and (m + f) < 50 and r >= 50:
        print("C")
    # 中間試験と期末試験の合計点数が 30 未満ならば成績は F
    elif (m + f) < 30:
        print("F")
