n,m,l = map(int,input().split())#n,m,lの入力
#n x m の行列を読み込む
A = [[int(i) for i in input().split()]for j in range(n)]

#m x l の行列を読み込む
B = [[int(i) for i in input().split()]for j in range(m)]

#n*lの行列の積をいれる行列Cを定義
C = [[0]*l for i in range(n)]

# C = np.dot(A,B) #行列の積を求める

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k]*B[k][j]

for i in range(n):
    print(C[i][0],end="")
    for j in range(1,l):
        print("",C[i][j],end="")
    print()
