#行数ｒ、列数ｃを入力
r,c = map(int,input().split())

#r x c の行列Aの入力
A = [[int(i) for i in input().split()]for j in range(r)]

#各行と各列をそれぞれたして行列に追加
for i in range(r):
    addr = 0 #行の合計
    for j in range(c):
        addr += A[i][j]
    A[i].append(addr) #各行の最後に追加

B = list(map(list,(zip(*A)))) #リストAの行列を転置したBを作成
for i in range(c+1): #行を追加してサイズが1増えたから
    addc = 0 #もとの列の合計(転置後の行の合計)
    for j in range(r):
        addc += B[i][j]
    B[i].append(addc) #リストに追加

A = list(map(list,(zip(*B)))) #Bを転置してもとに戻す

for i in range(r+1):
    for j in range(c+1):
        if j < c:
            print(A[i][j],end=" ")
        elif j == c:
            print(A[i][j])
    
