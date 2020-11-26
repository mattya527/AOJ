while True:
    n = int(input()) #数値の入力
    if n == 0: #０だった時終了
        break
    l = [int(i) for i in list(str(n))] #入力した数値を各桁ずつリストに入れる
    print(sum(l)) #リストの各桁を合計して出力
