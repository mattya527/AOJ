n,m = map(int,input().split())
c = []

#n x m の行列を読み込む
A = [[int(i) for i in input().split()]for j in range(n)]

#m x 1 の行列を読み込む
b = [int(input()) for i in range(m)]
for i in range(n):
    ci = 0
    for j in range(m):
         ci += A[i][j] * b[j]
    c.append(ci)

for i in range(n):
    print(c[i])
