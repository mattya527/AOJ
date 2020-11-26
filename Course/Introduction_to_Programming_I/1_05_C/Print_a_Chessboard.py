while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0: break
    for i in range(H):
        for j in range(W):
            if ((i+1) % 2 == 1 and (j+1) % 2 == 1) or ((i+1) % 2 == 0 and (j+1) % 2 == 0):
                print("#",end="")
            else:
                print(".",end="")
        print()
    print("")
