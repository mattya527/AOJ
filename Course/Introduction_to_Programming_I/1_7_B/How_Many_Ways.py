while True:
    #n,xの入力
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break
    count = 0
    #三重ループですべての組み合わせを試行
    for i in range(1,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n+1):
                if i+j+k == x:
                    count+=1

    print(count)
