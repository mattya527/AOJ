while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0: break
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b-1 or i == 0 or i == a -1:
                print(r"#",end="")
            else:
                print(r".",end="")
        print()
    print("")
